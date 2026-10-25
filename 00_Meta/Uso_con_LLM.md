---
tipo: meta
estado: borrador
aliases: [Uso con LLM, Consultar la biblioteca, LLM usage]
---
# Uso de la biblioteca con un LLM

## Tres formas de dar acceso a un modelo
| Forma | Cuándo | Cómo |
|---|---|---|
| **1. Paquete de contexto** (recomendada para empezar) | Cualquier chat con IA | `python3 scripts/consultar.py "pregunta" --contexto` y pegar la salida junto con el *prompt* de abajo |
| **2. Acceso al repositorio** | Agentes con acceso a archivos (Claude Code, etc.) | El agente lee `AGENTS.md`, consulta `indice.json` y abre las notas |
| **3. RAG / servidor MCP** | Uso intensivo o compartido | Indexar `indice.json` y las notas en un sistema de recuperación *(pendiente)* |

## Herramientas
- `scripts/indexar.py` → genera `indice.json`: título, tipo, metadatos, resumen, secciones y enlaces de entrada y salida de cada nota.
- `scripts/consultar.py "pregunta"` → detecta la edad (o el curso), las necesidades y las áreas; puntúa las notas, prioriza las de mejor evidencia, sigue los enlaces y **separa los mitos** de las recomendaciones. Opciones: `--contexto` (texto completo de las notas clave) y `--json`.
- `scripts/test_consultas.py` → batería de preguntas reales que deben encontrar las notas esenciales y no recomendar nunca un mito.

## *Prompt* recomendado
```
Eres un asesor pedagógico para docentes de Educación Primaria. Responde SOLO con la
información de las notas que te adjunto (biblioteca de pedagogía primaria).
Reglas:
1. Cita la nota en la que basas cada recomendación (ruta del archivo).
2. Indica el nivel de evidencia (A-D) de cada estrategia; si es D o ?, dilo.
3. Nunca recomiendes lo que aparece como mito (nivel M); si el docente lo menciona, explícale por qué no.
4. En necesidades educativas: orientaciones de aula, nunca diagnóstico; recuerda coordinar con orientación.
5. Si las notas están en estado "borrador", advierte de que no han sido revisadas.
6. Si la información no está en las notas, dilo en lugar de inventar.
7. Sé práctico: pasos concretos que el docente pueda aplicar mañana.

Pregunta del docente: <PREGUNTA>
Notas: <SALIDA DE consultar.py --contexto>
```

## Ejemplo completo
Pregunta: *"Tengo un alumno de 8 años con TDAH que no termina las tareas de matemáticas, ¿qué hago?"*

`consultar.py` detecta: edad 8 · necesidad `tdah` · área `matematicas`, y devuelve: [[TDAH]], [[Instruccion_Explicita]], [[Ejemplos_Resueltos]], [[Hechos_Numericos]], [[Enfoque_CPA]], [[Progresion_Matematicas]], [[Discalculia]], [[RTI_MTSS]] (≈2.400 palabras de contexto).

Respuesta generada **solo** con esas notas:

> ⚠️ Las notas consultadas están en borrador (no revisadas). Esto son orientaciones de aula, no un diagnóstico.
>
> **1. Divide la tarea** (`06_Diversidad/TDAH.md`). En lugar de una ficha de 20 operaciones, dale bloques de 4-5 con una comprobación tuya entre bloque y bloque. Menos ítems por página, consignas de una en una, en voz alta y por escrito (evidencia B).
>
> **2. Refuerza de inmediato y a menudo** (TDAH, evidencia A). Reconoce cada bloque terminado de forma concreta ("Has acabado las cinco y has revisado la tercera"). Un registro diario compartido con la familia ayuda a la continuidad.
>
> **3. Asegura que sabe hacerlo antes de pedirle que lo haga solo** (`04_Metodologias/Instruccion_Explicita.md`, A; `04_Metodologias/Ejemplos_Resueltos.md`, A). Muchas tareas sin terminar son tareas que el alumno no sabe resolver. Modela un ejemplo pensando en voz alta, haced uno juntos y deja en su mesa una tarjeta con el ejemplo resuelto.
>
> **4. Libera su memoria de trabajo** (`03_Areas/Hechos_Numericos.md`, A). Si a los 8 años todavía cuenta con los dedos para sumas sencillas, cada operación le cuesta el doble de atención. Dedica 5 minutos diarios a la práctica breve y espaciada de los hechos numéricos, con retroalimentación inmediata.
>
> **5. Introduce movimiento** (TDAH; `04_Metodologias/Pausas_Activas.md`, B). Pausas activas breves entre bloques; nunca le quites el recreo o la educación física como castigo.
>
> **6. Descarta otras causas.** Si las dificultades se dan sobre todo en matemáticas y no en otras áreas, revisa las señales de `06_Diversidad/Discalculia.md` y coméntalo con orientación ([[RTI_MTSS]]: registra su progreso con datos).

## Qué ha revelado la prueba (mejoras pendientes)
- Falta una nota sobre **tareas inacabadas y deberes** (la evidencia sobre los deberes en Primaria indica un impacto bajo).
- `Pausas_Activas` no aparece entre las notas clave aunque es relevante: el buscador es léxico, no semántico. Para un uso intensivo, conviene un sistema RAG con *embeddings*.

## Relacionado
- [[Arquitectura]] · [[Hoja_de_ruta]]
