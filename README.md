# Biblioteca de Pedagogía y Desarrollo Infantil (0-12)

Un Zettelkasten (bóveda de Obsidian) con el conocimiento necesario para **educar a niños y niñas de 0 a 12 años**: cómo se desarrollan, qué enseñar, cuándo, cómo, a quién y con qué evidencia. Sirve a la vez para **docentes** (Infantil y Primaria) y para **familias** que quieren criar a sus hijos de la mejor manera posible. El hilo conductor es el **desarrollo evolutivo** ([[MOC_Desarrollo]]).

**Es una bóveda de Obsidian lista para usar como segundo cerebro (Zettelkasten)**: descarga la carpeta, ábrela en Obsidian y sigue [[Guia_Obsidian]].

Lo usan tres tipos de lectores:
- **Familias**: empezar por [[MOC_Crianza]].
- **Docentes**: abrir la carpeta como bóveda en Obsidian. Se empieza por [[00_INICIO]].
- **Modelos LLM**: leer primero [AGENTS.md](AGENTS.md).

## Principios
1. **Universal primero, local después.** El conocimiento pedagógico (desarrollo infantil, metodologías, diversidad) es independiente del país. Los currículos nacionales (LOMLOE, Common Core…) son una capa aparte (`10_Curriculos/`) que se enlaza a ese núcleo.
2. **Evidencia explícita.** Toda afirmación sobre la eficacia de algo lleva un `nivel_evidencia` (ver [[Escala_de_evidencia|Escala de evidencia]]). Los mitos se documentan *como mitos*.
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
| `13_Mitos/` | Mitos educativos refutados (nivel M) |
| `14_Crianza/` | Crianza basada en evidencia (0-12) |
| `scripts/` | Validador de coherencia |
| `90_Plantillas/` | Plantillas de cada tipo de nota |
| `99_Inbox/` | Notas sin procesar |

## Consultar con IA
```bash
python3 scripts/consultar.py "Alumno de 8 años con TDAH que no termina las tareas de matemáticas" --contexto
```
Ver [[Uso_con_LLM]] para el *prompt* recomendado y las formas de dar acceso a un modelo.

## Validación
`python3 scripts/validar.py` revisa el frontmatter, los enlaces rotos y las fuentes obligatorias. En GitHub Actions se ejecutan además las pruebas de consulta y se comprueba que `indice.json` está actualizado.

## Privacidad
Nunca se incluyen datos de alumnos reales (ver [[Convenciones]]).

> ⚠️ Repositorio de apoyo a la práctica docente. No sustituye el diagnóstico ni la intervención de profesionales sanitarios o de orientación.
