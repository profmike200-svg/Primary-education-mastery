# Guía para agentes LLM

Esta bóveda es una base de conocimiento pedagógico para Educación Primaria (6-12 años). Antes de responder con ella:

## Herramientas (si puedes ejecutar Python)
- `python3 scripts/consultar.py "pregunta" --contexto` → devuelve las notas relevantes, detecta edad, necesidades y área y separa los mitos. Es el punto de partida más rápido.
- `indice.json` → índice de todas las notas (tipo, metadatos, resumen, enlaces). Regenerar con `python3 scripts/indexar.py` tras editar.
- Detalles y *prompt* recomendado: `00_Meta/Uso_con_LLM.md`.

## Cómo navegar
1. Empieza por `01_MOCs/00_INICIO.md` y baja por los MOCs. No recorras las carpetas a ciegas.
2. Cada nota tiene un **frontmatter YAML** (ver `00_Meta/Taxonomia.md`). Filtra por `tipo`, `edad_min`/`edad_max`, `area`, `necesidades`.
3. Los enlaces `[[Nota]]` apuntan al nombre del archivo, sin la extensión `.md`. Las secciones "Relacionado" y "Requisitos previos" forman el grafo.

## Reglas obligatorias
- **Respeta `nivel_evidencia`** (`00_Meta/Escala_de_evidencia.md`). No recomiendes como eficaz nada con nivel `M` (mito refutado). Si el nivel es `D` o `?`, dilo explícitamente.
- **Separa lo universal de lo local.** Para requisitos legales o curriculares de un país, usa solo `10_Curriculos/<PAIS>/`.
- **Diversidad**: ofrece orientaciones de aula. Nunca diagnostiques. Remite siempre a los especialistas.
- Si una nota tiene `estado: borrador`, avisa de que su contenido no está revisado.
- **Privacidad**: no escribas en la bóveda datos de alumnos reales, aunque el usuario los proporcione. Anonimiza y generaliza.
- No inventes fuentes: si no puedes verificar una referencia, deja `nivel_evidencia: "?"` y añade `pendiente_fuente: true`.
- Cita la nota (y su fuente en `11_Fuentes/`) en la que basas cada recomendación.

## Preguntas típicas y por dónde empezar
| Pregunta | Ruta |
|---|---|
| ¿Qué enseñar a los 8 años en matemáticas? | MOC_Areas → progresión del área → filtrar por edad |
| ¿Cómo enseñar X? | nota del contenido → `metodologias_recomendadas` |
| ¿Cómo adaptar para un alumno con TDAH? | MOC_Diversidad → nota de la necesidad → estrategias |
| Dame una sesión o actividad para X | `12_Practica/` filtrando por `area`, edad y `necesidades` |
| ¿Qué significa este término en otro país? | `00_Meta/Glosario_entre_sistemas.md` |
| ¿Funciona la metodología Y? | nota de la metodología → `nivel_evidencia` + sección Evidencia |
