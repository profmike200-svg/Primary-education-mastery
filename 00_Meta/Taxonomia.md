---
tipo: meta
estado: estable
---
# Taxonomía: valores permitidos en el frontmatter

Usar **solo** estos valores (en minúsculas y sin tildes) para que las consultas funcionen.

## `tipo`
`etapa` · `dimension_desarrollo` · `area` · `progresion` · `contenido` · `metodologia` · `estrategia` · `autor` · `corriente` · `necesidad` · `concepto` · `evaluacion` · `gestion_aula` · `curriculo` · `fuente` · `mito` · `practica` · `glosario` · `crianza` · `moc` · `meta`

## `area`
`matematicas` · `lengua` · `lectoescritura` · `lengua_extranjera` · `ciencias_naturales` · `ciencias_sociales` · `artistica` · `musica` · `educacion_fisica` · `valores_ciudadania` · `competencia_digital` · `socioemocional` · `transversal`

Áreas de Educación Infantil (LOMLOE): `crecimiento_en_armonia` · `descubrimiento_del_entorno` · `comunicacion_y_representacion`

Familia: `crianza`

## Edad
`edad_min` / `edad_max`: números enteros de 0 a 18 (el núcleo actual cubre 0-12; preparado para ampliarse a la adolescencia). Para bebés, `0` = primer año. El curso es orientativo (la edad es lo universal):
| Edad | España | EE. UU. | Reino Unido |
|---|---|---|---|
| 0-3 | Infantil, 1er ciclo (escuela infantil) | Infant / toddler care | Nursery |
| 3-6 | Infantil, 2º ciclo (3, 4 y 5 años) | Pre-K, Kindergarten | Nursery, Reception |
| 6-7 | 1º | 1st grade | Year 2 |
| 7-8 | 2º | 2nd | Year 3 |
| 8-9 | 3º | 3rd | Year 4 |
| 9-10 | 4º | 4th | Year 5 |
| 10-11 | 5º | 5th | Year 6 |
| 11-12 | 6º | 6th (middle) | Year 7 (secondary) |

## `dimension`
`cognitiva` · `linguistica` · `socioemocional` · `motora` · `moral` · `ejecutiva`

## `necesidades`
`tdah` · `tea` · `dislexia` · `discalculia` · `disgrafia` · `tdl` · `discapacidad_intelectual` · `altas_capacidades` · `discapacidad_sensorial` · `discapacidad_motora` · `incorporacion_tardia` · `vulnerabilidad_socioemocional`

## `nivel_evidencia`
`A` · `B` · `C` · `D` · `M` · `?` (ver [[Escala_de_evidencia|Escala de evidencia]])

## `estado`
`borrador` (redactado, fuentes sin comprobar) · `verificado_ia` (todas sus fuentes comprobadas en línea por la IA y el contenido revisado para que sea coherente con ellas) · `revisado` (leído y validado por el docente) · `estable`

## `verificado` (fichas de fuente)
`pendiente` · `parcial` (encontrada en fuentes secundarias) · `si` (cita y conclusiones comprobadas) · `corregida` (había un error y se ha corregido)

## Etiquetas (`tags`)
Solo para facetas que no tienen campo propio, por ejemplo `#cooperativo`, `#manipulativo`, `#juego`, `#exterior`. Se prefieren los campos a las etiquetas.
