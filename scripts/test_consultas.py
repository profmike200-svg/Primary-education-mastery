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
    ("Tengo un alumno de 7 años que se distrae todo el rato y no para quieto",
     ["Pausas_Activas"], []),
    ("¿Cuántos deberes debo mandar en 3º?",
     ["Deberes_y_Tareas_Inacabadas"], []),
    ("Mis alumnos de 5º no tienen hábito lector, no les gusta leer",
     ["Educacion_Literaria_y_Lectura_por_Placer"], []),
    ("Un alumno de 2º tiene rabietas y pega a sus compañeros",
     ["Gestion_de_la_Conducta", "Autorregulacion_Emocional"], []),
    ("¿Cómo hago una rúbrica para evaluar una exposición oral?",
     ["Rubricas"], []),
    ("¿Qué es la pirámide del aprendizaje?",
     [], ["Mito_Piramide_del_Aprendizaje"]),
    ("¿Cómo enseño a programar con Scratch a niños de 10 años?",
     ["Pensamiento_Computacional"], []),
    ("¿Qué dice la LOMLOE sobre matemáticas?",
     ["ES_LOMLOE_Matematicas"], []),
    ("Alumno sordo con audífonos en mi clase de 4º",
     ["Discapacidad_Auditiva"], []),
    ("¿Cómo trabajo el pensamiento histórico en 6º?",
     ["Pensamiento_Historico"], []),
    ("¿Puede repetir curso un alumno de 3º según la LOMLOE?",
     ["ES_Evaluacion_y_Promocion"], []),
    ("¿Cómo se estructura una situación de aprendizaje?",
     ["ES_Programacion_y_Situaciones_de_Aprendizaje"], []),
    ("¿Qué hago si sospecho que un alumno sufre maltrato en casa? Protocolo LOPIVI",
     ["ES_Proteccion_Infancia_y_Datos"], []),
    ("¿Cómo son las oposiciones de maestro de primaria?",
     ["ES_Acceso_a_la_Profesion"], []),
    ("¿Qué es un ACNEAE y qué es una adaptación curricular significativa?",
     ["ES_Atencion_a_la_Diversidad"], []),
    ("¿Cuáles son las competencias clave de la LOMLOE?",
     ["ES_Marco_Curricular_LOMLOE"], []),
    ("¿Qué es la PGA y el PEC del centro?",
     ["ES_Documentos_de_Centro"], []),
    ("Quiero irme a enseñar a Estados Unidos con el programa de profesores visitantes",
     ["ES_Acceso_a_la_Profesion"], []),
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
