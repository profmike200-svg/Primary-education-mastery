---
tipo: meta
estado: estable
aliases: [Guía de Obsidian, Cómo usar esta bóveda, Segundo cerebro]
---
# Cómo usar esta bóveda en Obsidian (segundo cerebro)

## 1. Abrirla por primera vez (5 minutos)
1. Instala Obsidian (gratis): obsidian.md. Hay versión para Windows, Mac, Linux, Android e iOS.
2. Descarga el repositorio: en GitHub, **Code → Download ZIP** y descomprímelo (o clónalo con GitHub Desktop).
3. En Obsidian: **Abrir carpeta como bóveda** → elige la carpeta descomprimida.
4. Cuando pregunte si confías en el autor, pulsa **Confiar**. Ya funciona: enlaces, grafo, notas que enlazan aquí, marcadores, plantillas y mapa visual vienen configurados.
5. **Opcional pero recomendado**: Ajustes → Plugins de la comunidad → Explorar → instala y activa **Dataview**. Hace funcionar las tablas automáticas (panel de control, consultas por edad, evidencia…).

## 2. Por dónde entrar
En la barra lateral, pestaña **Marcadores** (⭐):
- 🏛️ **Inicio**: [[00_INICIO]]
- 🗺️ **Mapa visual**: `Mapa_del_Segundo_Cerebro.canvas`, todo el conocimiento de un vistazo
- 📖 **Plan de lectura**: [[Plan_de_Lectura]]
- 🎒 Qué enseñar en cada curso · 👨‍👩‍👧 Crianza · 📝 Oposiciones

## 3. Las herramientas del segundo cerebro
| Herramienta | Para qué | Cómo |
|---|---|---|
| **Grafo** | Ver cómo se conecta todo. Los colores indican el tipo (rojo = desarrollo y mitos, azul = áreas, verde = metodologías y práctica, naranja = diversidad, rosa = crianza…) | Icono del grafo en la barra izquierda o `Ctrl/Cmd + G` |
| **Grafo local** | Ver solo lo conectado a la nota que lees | Menú de la nota → *Abrir grafo local* |
| **Enlaces entrantes** (*backlinks*) | Ver qué notas citan la actual: así se descubren conexiones | Panel derecho |
| **Vista previa al pasar el ratón** | Leer un enlace sin salir de la nota | `Ctrl/Cmd` + pasar el ratón |
| **Buscador rápido** | Saltar a cualquier nota | `Ctrl/Cmd + O` |
| **Búsqueda global** | Buscar texto en toda la bóveda (p. ej. `tdah`, `nivel_evidencia: "A"`) | `Ctrl/Cmd + Shift + F` |
| **Propiedades** | Los metadatos de cada nota (tipo, edad, área, evidencia, estado) | Arriba de cada nota |
| **Nota aleatoria** | Repasar y descubrir | Paleta de comandos → *Abrir nota aleatoria* |

## 4. El método Zettelkasten aplicado aquí
1. **Captura** (rápido, sin orden): usa la **nota diaria** (icono del calendario) o crea una nota en `99_Inbox/`. Una idea de una lectura, una pregunta del aula, algo que funcionó.
2. **Procesa** (una vez a la semana): convierte cada idea útil en una **nota atómica** con su plantilla (`Ctrl/Cmd + P` → *Insertar plantilla*): una idea por nota, con tus propias palabras.
3. **Conecta**: enlaza la nota con su MOC y con al menos dos notas relacionadas (escribe `[[` y Obsidian sugiere). **Una nota sin enlaces es una nota perdida.**
4. **Evidencia**: indica el `nivel_evidencia` y la fuente. Si no la sabes, `"?"`.
5. **Revisa**: cuando leas una nota y estés de acuerdo, cambia `estado` a `revisado`.

Más detalle: [[Arquitectura]] · [[Convenciones]] · [[Taxonomia]].

## 5. Reglas de oro
- **Nunca datos de alumnos reales** (ni en el diario). Ver [[Convenciones]].
- Enlaza siempre por el **nombre del archivo**: `[[Nombre_De_La_Nota]]` o `[[Nombre_De_La_Nota|texto que quieras]]`. Obsidian lo hace solo si eliges la sugerencia.
- No renombres archivos fuera de Obsidian: dentro de Obsidian, los enlaces se actualizan solos.

## 6. Sincronizar entre ordenador, móvil y GitHub
- **Lo más sencillo**: trabaja con la carpeta en el ordenador; cuando quieras actualizarla con lo nuevo de GitHub, vuelve a descargar el ZIP (o usa GitHub Desktop → *Fetch / Pull*).
- **Móvil**: Obsidian Sync (de pago) o copiar la carpeta a iCloud/Drive.
- **Avanzado**: el plugin comunitario **Obsidian Git** sincroniza la bóveda con GitHub automáticamente.

## 7. Usarla con una IA
Ver [[Uso_con_LLM]]: el buscador `scripts/consultar.py` prepara el contexto para cualquier asistente de IA.
