#!/usr/bin/env python3
"""Batería de preguntas reales de docentes para comprobar que la consulta encuentra lo esencial.

Uso: python3 scripts/test_consultas.py   (sale con código 1 si alguna falla)
"""
import sys

from consultar import consultar

# (pregunta, notas que deben aparecer en notas clave o práctica, mitos que deben señalarse)
CASOS = [
    ("Tengo un alumno de 8 años con TDAH que no termina las tareas de matemáticas, ¿qué hago?",
     ["TDAH", "Instruccion_Explicita"], []),
    ("¿Cómo enseño a leer en 1º de primaria?",
     ["Ensenanza_Fonetica_Sistematica", "Decodificacion"], []),
    ("¿Funcionan los estilos de aprendizaje visual auditivo kinestésico?",
     [], ["Mito_Estilos_de_Aprendizaje"]),
    ("Alumna de 10 años con dislexia, ¿cómo adapto los exámenes?",
     ["Dislexia"], []),
    ("¿Cómo enseñar fracciones a niños de 9 años?",
     ["Fracciones", "Sesion_Fracciones_Recta_Numerica"], []),
    ("Me voy a trabajar a Estados Unidos, ¿qué es un IEP y un plan 504?",
     ["Glosario_entre_sistemas"], []),
    ("Niño de 6 años con autismo que se descontrola en clase",
     ["TEA", "Autorregulacion_Emocional"], []),
    ("Ha llegado un alumno nuevo que no habla español",
     ["Incorporacion_Tardia"], []),
    ("¿Sirve el brain gym para que se concentren?",
     [], ["Mito_Brain_Gym"]),
    ("Mis alumnos de 4º escriben redacciones muy pobres, ¿cómo mejoro la escritura?",
     ["Composicion_Escrita", "Ensenanza_Estrategica_Escritura_SRSD"], []),
    ("¿Es mejor empezar inglés lo antes posible?",
     ["Progresion_Lengua_Extranjera"], ["Mito_Cuanto_Antes_Mejor_L2"]),
    ("¿Cómo trabajo la gestión de las emociones en primero?",
     ["Progresion_Socioemocional"], []),
    ("Hay un caso de acoso escolar en mi clase de 5º",
     ["Convivencia_y_Acoso"], []),
    ("Alumno de altas capacidades que se aburre en matemáticas",
     ["Altas_Capacidades"], []),
]


def main():
    fallos = 0
    for pregunta, esperadas, mitos in CASOS:
        r = consultar(pregunta)
        encontradas = {f["id"] for f in r["notas_clave"] + r["practica"]}
        mitos_r = {f["id"] for f in r["mitos_relacionados"]}
        faltan = [e for e in esperadas if e not in encontradas] + [m for m in mitos if m not in mitos_r]
        mito_recomendado = [f["id"] for f in r["notas_clave"] + r["practica"] if f["tipo"] == "mito"]
        ok = not faltan and not mito_recomendado
        fallos += not ok
        print(f"{'OK   ' if ok else 'FALLO'} {pregunta}")
        if faltan:
            print(f"        faltan: {faltan}")
            print(f"        obtenidas: {[f['id'] for f in r['notas_clave']]}")
        if mito_recomendado:
            print(f"        ¡mito recomendado!: {mito_recomendado}")
    print(f"\n{len(CASOS) - fallos}/{len(CASOS)} consultas correctas")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
