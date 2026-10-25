#!/usr/bin/env python3
"""Consulta la bóveda con una pregunta en lenguaje natural y devuelve un paquete de contexto.

Detecta la edad (o el curso), las necesidades y las áreas mencionadas, puntúa las notas,
sigue los enlaces de un salto y separa los mitos de las recomendaciones.

Uso:
  python3 scripts/consultar.py "Alumno de 8 años con TDAH que no termina las tareas de matemáticas"
  python3 scripts/consultar.py "..." --contexto      # añade el texto completo de las notas clave
  python3 scripts/consultar.py "..." --json          # salida estructurada
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
INDICE = RAIZ / "indice.json"

VACIAS = set("""a al algo ante como con cual cuando de del desde donde el ella ellos en entre es esa ese
eso esta este esto estoy hay hace hacer hago la las le les lo los mas me mi mis muy no nos o para pero
por porque que se ser si sin sobre su sus tambien tengo tiene un una uno unos y ya yo the of and to in
puedo debo deberia quiero alguna algun cosas tarea tareas clase aula alumno alumna alumnos
alumnas nino nina ninos ninas hijo hija ano anos curso funciona funcionan sirve sirven""".split())

NECESIDADES = {
    "tdah": ["tdah", "hiperactiv", "deficit de atencion", "adhd", "impulsiv"],
    "tea": ["tea", "autis", "asperger", "espectro autista"],
    "dislexia": ["dislex"],
    "discalculia": ["discalcul"],
    "disgrafia": ["disgraf"],
    "tdl": ["tdl", "tel", "trastorno del lenguaje", "trastorno del desarrollo del lenguaje"],
    "altas_capacidades": ["altas capacidades", "aacc", "superdotad", "sobredotad", "gifted", "se aburre"],
    "discapacidad_intelectual": ["discapacidad intelectual"],
    "discapacidad_sensorial": ["sordo", "sorda", "sordera", "hipoacusia", "audifono", "ciego", "ciega",
                               "ceguera", "baja vision"],
    "discapacidad_motora": ["paralisis cerebral", "silla de ruedas", "discapacidad motora", "discapacidad fisica"],
    "incorporacion_tardia": ["recien llegad", "no habla espanol", "no habla castellano", "inmigrante",
                             "migrante", "incorporacion tardia", "english learner", "esl", "ell"],
    "vulnerabilidad_socioemocional": ["trauma", "ansiedad", "maltrato", "duelo", "adversidad", "triste"],
}
NOTA_NECESIDAD = {
    "tdah": "TDAH", "tea": "TEA", "dislexia": "Dislexia", "discalculia": "Discalculia", "disgrafia": "Disgrafia",
    "tdl": "TDL", "altas_capacidades": "Altas_Capacidades", "discapacidad_intelectual": "Discapacidad_Intelectual",
    "discapacidad_motora": "Discapacidad_Motora", "incorporacion_tardia": "Incorporacion_Tardia",
    "vulnerabilidad_socioemocional": "Vulnerabilidad_Socioemocional",
}
AREAS = {
    "matematicas": ["matemat", "mates", "fraccion", "suma", "resta", "multiplic", "division", "numer",
                    "calcul", "geometr", "tablas", "problemas"],
    "lectoescritura": ["leer", "lectur", "lector", "letra", "fonolog", "decodific"],
    "lengua": ["escrib", "escritura", "redacci", "ortograf", "gramatic", "vocabulario", "oral"],
    "lengua_extranjera": ["ingles", "english", "idioma", "lengua extranjera"],
    "ciencias_naturales": ["ciencia", "experiment", "naturales", "indagacion"],
    "ciencias_sociales": ["historia", "geografia", "sociales"],
    "socioemocional": ["emocion", "rabieta", "enfad", "autorregul", "descontrol", "conflicto", "frustra"],
    "educacion_fisica": ["educacion fisica", "deporte", "motric", "moverse"],
    "musica": ["musica", "cantar"],
    "artistica": ["plastica", "dibujo", "arte"],
    "competencia_digital": ["digital", "internet", "programacion", "pantalla", "tablet", "ordenador"],
    "valores_ciudadania": ["ciudadan", "valores", "asamblea"],
}
PESO_EVIDENCIA = {"A": 1.5, "B": 1.25, "C": 1.0, "D": 0.85, "?": 0.9, "M": 1.0}
TIPOS_RECOMENDABLES = {"metodologia", "estrategia", "practica", "contenido", "evaluacion", "gestion_aula"}


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in texto if not unicodedata.combining(c))


def raiz(token):
    return token[:6] if len(token) > 6 else token


def tokens(texto):
    return [t for t in re.findall(r"[a-z0-9]+", normalizar(texto)) if t not in VACIAS and len(t) > 2]


def contiene(texto_norm, patron):
    return re.search(r"(?<![a-z])" + re.escape(patron), texto_norm) is not None


def detectar(pregunta):
    q = normalizar(pregunta)
    edad = None
    if m := re.search(r"(\d{1,2})\s*anos", q):
        edad = int(m.group(1))
    elif m := re.search(r"\b([1-6])\s*(?:o|º|°)?\s*(?:de primaria|curso)?\b", q.replace("º", "o ")):
        if re.search(r"\b[1-6]\s*(o|º|°)\b|de primaria|curso", q.replace("º", "o ")):
            edad = int(m.group(1)) + 5
    if m := re.search(r"\b(\d)(?:st|nd|rd|th) grade", q):
        edad = int(m.group(1)) + 6
    necesidades = [n for n, pats in NECESIDADES.items()
                   if any(re.search(r"(?<![a-z])" + re.escape(p) + (r"(?![a-z])" if len(p) <= 4 else ""), q) for p in pats)]
    areas = [a for a, pats in AREAS.items() if any(contiene(q, p) for p in pats)]
    return {"edad": edad, "necesidades": necesidades, "areas": areas}


def en_rango(meta, edad):
    if edad is None:
        return True
    try:
        e0, e1 = int(meta.get("edad_min") or 0), int(meta.get("edad_max") or 99)
    except ValueError:
        return True
    return e0 - 1 <= edad <= e1


def texto_nota(nota):
    return (RAIZ / nota["ruta"]).read_text(encoding="utf-8")


CURRICULO = ["lomloe", "ley", "curricul", "decreto", "common core", "ngss", "wida", "estandar", "eeuu",
             "estados unidos", "espana", "normativa"]


def puntuar(indice, pregunta, det):
    q_raices = {raiz(t) for t in tokens(pregunta)}
    # Palabras de área o necesidad no bastan para traer un mito: debe coincidir su tema concreto.
    genericas = {raiz(t) for pats in list(AREAS.values()) + list(NECESIDADES.values()) for p in pats for t in tokens(p)}
    q_especificas = q_raices - genericas
    pide_curriculo = any(contiene(normalizar(pregunta), p) for p in CURRICULO)
    puntos, en_titulo = {}, {}
    for nid, n in indice.items():
        meta = n["metadatos"]
        if n["tipo"] in ("meta", "moc", "fuente") or n["ruta"].startswith("90_"):
            continue
        if not en_rango(meta, det["edad"]):
            continue
        titulo = {raiz(t) for t in tokens(n["titulo"] + " " + " ".join(n["aliases"]) + " " + nid.replace("_", " "))}
        cuerpo = [raiz(t) for t in tokens(texto_nota(n))]
        en_titulo[nid] = len(q_raices & titulo)
        s = 5 * en_titulo[nid]
        s += min(sum(1 for t in cuerpo if t in q_raices), 30) * 0.25
        areas_nota = set(meta.get("area") or []) if isinstance(meta.get("area"), list) else {meta.get("area")}
        s += 3 * len(areas_nota & set(det["areas"]))
        nec_nota = set()
        for campo in ("necesidad", "necesidades_compatibles", "necesidades_contempladas"):
            v = meta.get(campo)
            nec_nota |= set(v) if isinstance(v, list) else ({v} if v else set())
        s += 4 * len(nec_nota & set(det["necesidades"]))
        if NOTA_NECESIDAD.get(next(iter(nec_nota), None)) == nid and nec_nota & set(det["necesidades"]):
            s += 10
        if s <= 0:
            continue
        if n["tipo"] == "curriculo" and not pide_curriculo:
            s *= 0.3
        if n["tipo"] == "practica" and det["areas"] and not areas_nota & set(det["areas"]):
            continue
        if n["tipo"] == "mito" and (not q_especificas & titulo or en_titulo[nid] < 2):
            continue
        if n["tipo"] in TIPOS_RECOMENDABLES:
            s *= PESO_EVIDENCIA.get(meta.get("nivel_evidencia", "?"), 1.0)
        puntos[nid] = s
    # Un salto por el grafo: las notas enlazadas por las mejores heredan una parte de su puntuación.
    mejores = sorted(puntos, key=puntos.get, reverse=True)[:8]
    for nid in mejores:
        for destino in indice[nid]["enlaces"]:
            if destino in puntos:
                puntos[destino] += puntos[nid] * 0.1
    return puntos


def consultar(pregunta, maximo=8):
    indice = json.loads(INDICE.read_text(encoding="utf-8"))["notas"]
    det = detectar(pregunta)
    puntos = puntuar(indice, pregunta, det)
    orden = sorted(puntos, key=puntos.get, reverse=True)
    mitos = [n for n in orden if indice[n]["tipo"] == "mito"][:3]
    claves = [n for n in orden if indice[n]["tipo"] not in ("mito", "practica")][:maximo]
    for nec in det["necesidades"]:
        nota = NOTA_NECESIDAD.get(nec)
        if nota in indice and nota not in claves:
            claves.insert(0, nota)
    practica = [n for n in orden if indice[n]["tipo"] == "practica"][:3]

    def ficha(nid):
        n = indice[nid]
        return {"id": nid, "ruta": n["ruta"], "titulo": n["titulo"], "tipo": n["tipo"],
                "nivel_evidencia": n["metadatos"].get("nivel_evidencia", ""), "estado": n["metadatos"].get("estado", ""),
                "resumen": n["resumen"], "puntuacion": round(puntos.get(nid, 0), 1)}

    return {"pregunta": pregunta, "detectado": det, "notas_clave": [ficha(n) for n in claves[:maximo]],
            "practica": [ficha(n) for n in practica], "mitos_relacionados": [ficha(n) for n in mitos]}


def imprimir(res, contexto):
    d = res["detectado"]
    print(f"# Consulta: {res['pregunta']}\n")
    print(f"Detectado → edad: {d['edad'] or '—'} · necesidades: {', '.join(d['necesidades']) or '—'} · "
          f"áreas: {', '.join(d['areas']) or '—'}\n")
    for titulo, clave in (("Notas clave", "notas_clave"), ("Práctica de aula", "practica"),
                          ("⚠️ Mitos relacionados (NO recomendar)", "mitos_relacionados")):
        if not res[clave]:
            continue
        print(f"## {titulo}")
        for f in res[clave]:
            ev = f" · evidencia {f['nivel_evidencia']}" if f["nivel_evidencia"] else ""
            print(f"- **{f['titulo']}** ({f['tipo']}{ev} · {f['estado']}) — `{f['ruta']}`")
            if f["resumen"]:
                print(f"  {f['resumen']}")
        print()
    if contexto:
        print("---\n# Contexto completo\n")
        for f in res["notas_clave"][:5] + res["practica"][:1] + res["mitos_relacionados"]:
            print(f"<nota ruta=\"{f['ruta']}\">\n{(RAIZ / f['ruta']).read_text(encoding='utf-8').strip()}\n</nota>\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pregunta")
    ap.add_argument("--max", type=int, default=8)
    ap.add_argument("--contexto", action="store_true", help="incluye el texto completo de las notas clave")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if not INDICE.exists():
        sys.exit("Falta indice.json: ejecuta primero python3 scripts/indexar.py")
    res = consultar(args.pregunta, args.max)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        imprimir(res, args.contexto)


if __name__ == "__main__":
    main()
