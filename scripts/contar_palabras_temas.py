#!/usr/bin/env python3
"""Cuenta las palabras del texto de examen de cada tema desarrollado (CLM_Tema_NN.md).

Se cuenta desde '## 1. Introduction' hasta el final de la conclusión (antes del
recuadro 'Key points'). No cuentan el mapa de memoria, los puntos clave ni las
referencias. Rango objetivo: 1500-2000 palabras.
Uso: python3 scripts/contar_palabras_temas.py [--estricto]
"""
import re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CARPETA = RAIZ / "10_Curriculos/ES_CLM/Temas"
MIN, MAX = 1500, 2000

def cuerpo(texto):
    ini = texto.find("## 1. Introduction")
    if ini < 0:
        return ""
    fin = texto.find("> ✅", ini)
    if fin < 0:
        fin = len(texto)
    t = texto[ini:fin]
    t = re.sub(r"^#+ .*$", "", t, flags=re.M)          # encabezados
    t = re.sub(r"^\|[-| ]+\|$", "", t, flags=re.M)     # separadores de tabla
    t = re.sub(r"[*_|>#`]", " ", t)
    return t

def contar(ruta):
    return len(re.findall(r"[A-Za-zÀ-ÿ0-9’'%-]+", cuerpo(ruta.read_text(encoding="utf-8"))))

def main():
    fallos = 0
    for ruta in sorted(CARPETA.glob("CLM_Tema_[0-9][0-9].md")):
        n = contar(ruta)
        ok = MIN <= n <= MAX
        fallos += not ok
        print(f"{'✅' if ok else '❌'} {ruta.stem}: {n} palabras")
    if "--estricto" in sys.argv and fallos:
        sys.exit(1)

if __name__ == "__main__":
    main()
