---
tipo: meta
estado: estable
aliases: [Escala de evidencia]
---
# Escala de evidencia

Campo `nivel_evidencia` del frontmatter. Se aplica a afirmaciones de **eficacia** (metodologías, estrategias, intervenciones).

| Nivel | Significado | Ejemplos de base |
|---|---|---|
| **A** | Evidencia sólida y consistente | Metaanálisis o revisiones sistemáticas que concuerdan (EEF, What Works Clearinghouse, Hattie con cautela) |
| **B** | Evidencia moderada | Varios ensayos controlados o cuasiexperimentales con resultados mayoritariamente positivos |
| **C** | Evidencia limitada o mixta | Pocos estudios, muestras pequeñas o resultados contradictorios |
| **D** | Fundamento teórico o de experiencia, sin evaluación empírica rigurosa | Tradición, opinión experta, estudios de caso |
| **M** | **Mito refutado**: la evidencia contradice la afirmación | Estilos de aprendizaje (VAK), pirámide del aprendizaje, "solo usamos el 10% del cerebro", Brain Gym |
| **?** | Sin evaluar todavía | Valor por defecto en borradores |

## Reglas
- Una metodología puede tener **niveles distintos según el componente o el contexto**. Se detallan en la sección "Evidencia" de la nota (p. ej. "ABP: C en general; B si incluye instrucción explícita de andamiaje").
- Toda nota con nivel A, B o M debe enlazar al menos una fuente de `11_Fuentes/`.
- Los mitos tienen su propia nota (`tipo: mito`) explicando por qué son falsos y qué los sustituye.
- Las teorías del desarrollo (Piaget, Vygotsky…) usan `vigencia` en lugar de eficacia: `vigente`, `revisada` o `superada en parte`.
