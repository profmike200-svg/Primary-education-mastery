# Biblioteca de Pedagogía Primaria

Un Zettelkasten (bóveda de Obsidian) con el conocimiento que un docente de Educación Primaria (6-12 años) necesita: qué enseñar, cuándo, cómo, a quién y con qué evidencia.

Lo usan dos tipos de lectores:
- **Docentes**: abrir la carpeta como bóveda en Obsidian. Se empieza por [[00_INICIO]].
- **Modelos LLM**: leer primero [AGENTS.md](AGENTS.md).

## Principios
1. **Universal primero, local después.** El conocimiento pedagógico (desarrollo infantil, metodologías, diversidad) es independiente del país. Los currículos nacionales (LOMLOE, Common Core…) son una capa aparte (`10_Curriculos/`) que se enlaza a ese núcleo.
2. **Evidencia explícita.** Toda afirmación sobre la eficacia de algo lleva un `nivel_evidencia` (ver [[Escala de evidencia]]). Los mitos se documentan *como mitos*.
3. **Notas atómicas.** Una idea por nota, enlazada con otras.
4. **Jerarquía por MOCs**, no por carpetas profundas (ver [[Arquitectura]]).

## Estructura
| Carpeta | Contenido |
|---|---|
| `00_Meta/` | Normas del sistema: arquitectura, convenciones, escala de evidencia, taxonomía |
| `01_MOCs/` | Mapas de contenido (índices navegables) |
| `02_Desarrollo/` | Etapas y dimensiones del desarrollo infantil |
| `03_Areas/` | Áreas de conocimiento y sus progresiones de aprendizaje |
| `04_Metodologias/` | Metodologías y estrategias didácticas |
| `05_Autores/` | Autores y corrientes |
| `06_Diversidad/` | Necesidades educativas y respuestas inclusivas |
| `07_Evaluacion/` | Evaluación |
| `08_Gestion_Aula/` | Clima, convivencia, rutinas, familias |
| `09_Conceptos/` | Conceptos transversales (memoria de trabajo, andamiaje…) |
| `10_Curriculos/` | Capa curricular por país |
| `11_Fuentes/` | Fichas bibliográficas |
| `12_Practica/` | Situaciones de aprendizaje, sesiones y actividades concretas |
| `scripts/` | Validador de coherencia |
| `90_Plantillas/` | Plantillas de cada tipo de nota |
| `99_Inbox/` | Notas sin procesar |

## Validación
`python3 scripts/validar.py` revisa el frontmatter, los enlaces rotos y las fuentes obligatorias. Se ejecuta en GitHub Actions con cada *push*.

## Privacidad
Nunca se incluyen datos de alumnos reales (ver [[Convenciones]]).

> ⚠️ Repositorio de apoyo a la práctica docente. No sustituye el diagnóstico ni la intervención de profesionales sanitarios o de orientación.
