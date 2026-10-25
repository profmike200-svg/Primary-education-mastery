---
tipo: meta
estado: estable
---
# Arquitectura

## Tres niveles de jerarquía
Las carpetas son **planas** (un nivel) y agrupan solo por *tipo* de nota. La jerarquía real se construye con enlaces:

```
00_INICIO  (índice maestro)
   └── MOC temático  (p. ej. MOC_Metodologias)
         └── MOC de subtema, si hace falta  (p. ej. MOC_Aprendizaje_Cooperativo)
               └── Notas atómicas  (p. ej. Rompecabezas_Jigsaw)
```

- **Nivel 1: el índice maestro** (`00_INICIO`). Solo enlaza a MOCs.
- **Nivel 2: MOCs temáticos**, uno por carpeta de contenido.
- **Nivel 3: notas atómicas**, cada una sobre una sola idea.
- Un sub-MOC se crea **solo** cuando un MOC pasa de unos 25 enlaces.

## Los dos ejes que lo conectan todo
Cualquier nota de contenido o metodología se sitúa en:
1. **Edad / desarrollo** (`edad_min`, `edad_max` + enlace a la etapa de `02_Desarrollo`)
2. **Área** (`area` + enlace a la progresión de `03_Areas`)

Con estos ejes un LLM puede responder "qué, cuándo y cómo" cruzando metadatos.

## Capa universal y capa local
- Núcleo universal: `02`–`09`. Nunca menciona leyes concretas como requisito.
- Capa práctica: `12_Practica/`. Situaciones y actividades concretas que aplican el núcleo; son universales salvo que indiquen `pais`.
- Capa local: `10_Curriculos/<PAIS>/`. Cada nota curricular enlaza a las notas universales equivalentes con `equivale_a:`. Así, para trabajar en EE. UU. solo hay que añadir la capa `US_CCSS`.

## Flujo de trabajo (para que no se convierta en un caos)
1. **Captura**: cualquier idea o lectura va a `99_Inbox/`, sin formato.
2. **Procesado** (semanal): convertir lo capturado en una nota atómica con la plantilla correspondiente, crear su ficha de fuente y asignarle un `nivel_evidencia`.
3. **Enlazado**: al menos 1 MOC padre y 2 notas relacionadas. Una nota sin enlaces es una nota huérfana y se considera no terminada.
4. **Revisión**: `estado` pasa de `borrador` → `revisado` → `estable`. **Solo el docente responsable** sube una nota a `revisado`; el contenido generado por IA entra siempre como `borrador`.
5. **Validación**: `python3 scripts/validar.py` antes de cada commit.

## Orden de construcción por capas
1. Meta + plantillas + MOCs vacíos ✅
2. Esqueleto: etapas del desarrollo y lista de metodologías, autores y necesidades (solo títulos y metadatos)
3. **Corte vertical piloto**: un tema desarrollado de punta a punta (p. ej. lectoescritura 6-8: desarrollo, progresión, metodologías, dislexia, evaluación, práctica y equivalencias ES/US) para validar el formato
4. Progresiones de aprendizaje por área
5. Desarrollo en profundidad, área por área
6. Capas curriculares por país
