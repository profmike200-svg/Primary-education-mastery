---
tipo: meta
estado: estable
---
# Panel de control
Requiere el plugin **Dataview**.

## Borradores pendientes de revisión
```dataview
TABLE tipo, nivel_evidencia FROM "" WHERE estado = "borrador" AND tipo != "moc" AND !contains(file.folder, "90_") SORT file.mtime DESC
```

## Notas sin evidencia asignada
```dataview
LIST FROM "04_Metodologias" OR "06_Diversidad" WHERE nivel_evidencia = "?"
```

## Notas huérfanas (sin enlaces entrantes)
```dataview
LIST FROM "" WHERE length(file.inlinks) = 0 AND tipo != "meta" AND !contains(file.folder, "90_")
```

## Metodologías por nivel de evidencia
```dataview
TABLE nivel_evidencia, edad_min, edad_max FROM "04_Metodologias" SORT nivel_evidencia ASC
```
