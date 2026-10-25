#!/usr/bin/env python3
"""Valida la coherencia de la bóveda: frontmatter, taxonomía, enlaces y fuentes.

Uso: python3 scripts/validar.py   (sale con código 1 si hay errores)
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
IGNORAR = {".git", ".obsidian", "90_Plantillas", ".github", "scripts"}
SIN_FRONTMATTER = {"README.md", "AGENTS.md"}

TIPOS = {"etapa", "dimension_desarrollo", "area", "progresion", "contenido", "metodologia",
         "estrategia", "autor", "corriente", "necesidad", "concepto", "evaluacion", "gestion_aula",
         "curriculo", "fuente", "mito", "practica", "glosario", "moc", "meta"}
AREAS = {"matematicas", "lengua", "lectoescritura", "lengua_extranjera", "ciencias_naturales",
         "ciencias_sociales", "artistica", "musica", "educacion_fisica", "valores_ciudadania",
         "competencia_digital", "socioemocional", "transversal"}
NECESIDADES = {"tdah", "tea", "dislexia", "discalculia", "disgrafia", "tdl", "discapacidad_intelectual",
               "altas_capacidades", "discapacidad_sensorial", "discapacidad_motora",
               "incorporacion_tardia", "vulnerabilidad_socioemocional"}
EVIDENCIA = {"A", "B", "C", "D", "M", "?"}
ESTADOS = {"borrador", "revisado", "estable"}
CAMPOS_NECESIDAD = ("necesidad", "necesidades", "necesidades_compatibles", "necesidades_contempladas")

ENLACE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def leer_frontmatter(texto):
    """Parser YAML mínimo (clave: valor y listas en línea), sin dependencias externas."""
    if not texto.startswith("---\n"):
        return None
    fin = texto.find("\n---", 4)
    if fin == -1:
        return None
    datos = {}
    for linea in texto[4:fin].splitlines():
        if ":" not in linea or linea.startswith((" ", "-")):
            continue
        clave, valor = linea.split(":", 1)
        valor = valor.strip().strip('"').strip("'")
        if valor.startswith("[") and valor.endswith("]"):
            valor = [v.strip().strip('"').strip("'") for v in valor[1:-1].split(",") if v.strip()]
        datos[clave.strip()] = valor
    return datos


def como_lista(valor):
    if valor in (None, ""):
        return []
    return valor if isinstance(valor, list) else [valor]


def main():
    notas = [p for p in RAIZ.rglob("*.md") if not IGNORAR & set(p.relative_to(RAIZ).parts)]
    nombres = {p.stem for p in notas}
    errores, avisos = [], []

    for p in notas:
        rel = p.relative_to(RAIZ)
        texto = p.read_text(encoding="utf-8")
        fm = leer_frontmatter(texto)
        if fm is not None:
            nombres.update(como_lista(fm.get("aliases")))

    for p in notas:
        rel = p.relative_to(RAIZ)
        texto = p.read_text(encoding="utf-8")
        fm = leer_frontmatter(texto)
        if fm is None:
            if rel.name not in SIN_FRONTMATTER:
                errores.append(f"{rel}: falta frontmatter")
            fm = {}
        else:
            tipo = fm.get("tipo")
            if tipo not in TIPOS:
                errores.append(f"{rel}: tipo inválido '{tipo}'")
            if fm.get("estado") and fm["estado"] not in ESTADOS and tipo != "fuente":
                errores.append(f"{rel}: estado inválido '{fm['estado']}'")
            for a in como_lista(fm.get("area")):
                if a not in AREAS:
                    errores.append(f"{rel}: área inválida '{a}'")
            for campo in CAMPOS_NECESIDAD:
                for n in como_lista(fm.get(campo)):
                    if n not in NECESIDADES:
                        errores.append(f"{rel}: necesidad inválida '{n}' en '{campo}'")
            ev = fm.get("nivel_evidencia")
            if ev not in (None, "") and ev not in EVIDENCIA:
                errores.append(f"{rel}: nivel_evidencia inválido '{ev}'")
            if ev in {"A", "B", "M"} and not como_lista(fm.get("fuentes")):
                errores.append(f"{rel}: nivel {ev} exige al menos una fuente en 'fuentes'")
            for campo in ("edad_min", "edad_max"):
                v = fm.get(campo)
                if v not in (None, "") and not (str(v).isdigit() and 5 <= int(v) <= 13):
                    errores.append(f"{rel}: {campo} debe ser un entero entre 5 y 13")

        sin_codigo = re.sub(r"```.*?```", "", texto, flags=re.S)
        sin_codigo = re.sub(r"`[^`\n]*`", "", sin_codigo)
        sin_codigo = re.sub(r"<!--.*?-->", "", sin_codigo, flags=re.S)
        for destino in ENLACE.findall(sin_codigo):
            destino = destino.strip()
            if destino and destino not in nombres:
                avisos.append(f"{rel}: enlace a nota inexistente [[{destino}]]")

    for a in avisos:
        print(f"AVISO  {a}")
    for e in errores:
        print(f"ERROR  {e}")
    print(f"\n{len(notas)} notas · {len(errores)} errores · {len(avisos)} avisos")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
