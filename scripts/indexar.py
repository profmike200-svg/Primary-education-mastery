#!/usr/bin/env python3
"""Genera indice.json: un índice estructurado de toda la bóveda para LLMs y herramientas.

Uso: python3 scripts/indexar.py
"""
import json
import re
from pathlib import Path

from validar import ENLACE, IGNORAR, RAIZ, como_lista, leer_frontmatter

SALIDA = RAIZ / "indice.json"


def cuerpo_sin_frontmatter(texto):
    if texto.startswith("---\n"):
        fin = texto.find("\n---", 4)
        if fin != -1:
            return texto[fin + 4:].lstrip("\n")
    return texto


def resumen(cuerpo, max_chars=300):
    """Primer párrafo de texto real tras el título (sin avisos ni encabezados)."""
    for bloque in re.split(r"\n\s*\n", cuerpo):
        bloque = "\n".join(l for l in bloque.splitlines() if not l.startswith("#")).strip()
        if not bloque or bloque.startswith((">", "|", "```", "<!--", "---")):
            continue
        texto = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), bloque)
        texto = re.sub(r"\s+", " ", texto.replace("**", ""))
        return texto[:max_chars] + ("…" if len(texto) > max_chars else "")
    return ""


def construir():
    notas = sorted(p for p in RAIZ.rglob("*.md") if not IGNORAR & set(p.relative_to(RAIZ).parts))
    indice = {}
    for p in notas:
        texto = p.read_text(encoding="utf-8")
        fm = leer_frontmatter(texto) or {}
        cuerpo = cuerpo_sin_frontmatter(texto)
        titulo = next((l[2:].strip() for l in cuerpo.splitlines() if l.startswith("# ")), p.stem)
        sin_codigo = re.sub(r"```.*?```|`[^`\n]*`|<!--.*?-->", "", cuerpo, flags=re.S)
        indice[p.stem] = {
            "ruta": str(p.relative_to(RAIZ)),
            "titulo": titulo,
            "tipo": fm.get("tipo", ""),
            "aliases": como_lista(fm.get("aliases")),
            "metadatos": {k: v for k, v in fm.items() if k not in ("aliases", "tipo")},
            "resumen": resumen(cuerpo),
            "secciones": [l.lstrip("#").strip() for l in cuerpo.splitlines() if l.startswith("## ")],
            "enlaces": sorted({d.strip() for d in ENLACE.findall(sin_codigo)}),
            "enlazada_desde": [],
        }

    alias_a_id = {a: k for k, v in indice.items() for a in v["aliases"]}
    for origen, nota in indice.items():
        nota["enlaces"] = sorted({alias_a_id.get(d, d) for d in nota["enlaces"]})
        for destino in nota["enlaces"]:
            if destino in indice and origen not in indice[destino]["enlazada_desde"]:
                indice[destino]["enlazada_desde"].append(origen)
    for nota in indice.values():
        nota["enlazada_desde"].sort()
    return indice


def main():
    indice = construir()
    SALIDA.write_text(json.dumps({"version": 1, "notas": indice}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{SALIDA.name}: {len(indice)} notas")


if __name__ == "__main__":
    main()
