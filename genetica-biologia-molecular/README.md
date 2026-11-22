# Genética y Biología Molecular (Medicina UNAL, 2026)

Una guía de estudio y un mazo de Anki, construidos a partir de las diapositivas de clase, con los datos verificados contra fuentes primarias, y ajustados a lo que evaluó el parcial final I-2026.

| Archivo | Qué es |
|---|---|
| [`Guia_de_estudio.md`](Guia_de_estudio.md) | **La guía completa**: los 8 capítulos en un solo archivo, con índice general, conexiones entre clases, tabla de enfermedades, fe de erratas y el [parcial final I-2026 resuelto](Guia_de_estudio.md#anexo-f-parcial-final-i-2026-resuelto) |
| [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg) | **El mazo completo**: 1.156 tarjetas Basic, un submazo por capítulo |

| # | Clase | Capítulo en la guía | Tarjetas |
|---|---|---|---|
| 1 | Introducción a la bioinformática y medicina genómica | [capítulo 1](Guia_de_estudio.md#1-introducción-a-la-bioinformática-y-medicina-genómica) | 68 |
| 2 | Genética del desarrollo | [capítulo 2](Guia_de_estudio.md#2-genética-del-desarrollo) | 93 |
| 3 | Ciclo celular | [capítulo 3](Guia_de_estudio.md#3-ciclo-celular-fases-motor-molecular-y-puntos-de-control) | 131 |
| 4 | Errores innatos del metabolismo | [capítulo 4](Guia_de_estudio.md#4-errores-innatos-del-metabolismo-eim) | 115 |
| 5 | Mecanismos de reparación del ADN | [capítulo 5](Guia_de_estudio.md#5-mecanismos-de-reparación-del-adn-de-la-lesión-molecular-a-la-clínica) | 367 |
| 6 | Genética del cáncer: hallmarks y perspectivas terapéuticas | [capítulo 6](Guia_de_estudio.md#6-genética-del-cáncer-biología-molecular-hallmarks-y-perspectivas-terapéuticas) | 158 |
| 7 | Técnicas de biología molecular | [capítulo 7](Guia_de_estudio.md#7-técnicas-de-biología-molecular) | 150 |
| 8 | Bases moleculares y variación genética (sin diapositivas: temas del parcial) | [capítulo 8](Guia_de_estudio.md#8-bases-moleculares-y-variación-genética) | 74 |
| | **Total** | | **1.156** |

Las 106 tarjetas de los temas que evaluó el parcial final I-2026 llevan la etiqueta `parcial`.

## Importar el mazo

Descarga [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg) y ábrelo con Anki (escritorio, AnkiDroid o AnkiMobile). Crea el mazo *Genética y Biología Molecular (UNAL 2026)* con los submazos 01 a 08.

Todas las tarjetas usan el tipo de nota *Genética Básico* (dos campos, una tarjeta por nota, igual que Basic), con modo nocturno. Cada nota tiene un id fijo: al reimportar una versión nueva, Anki actualiza las notas existentes y agrega las nuevas **sin duplicar ni borrar tu progreso**.

### Si ya habías importado una versión anterior

**Capítulos 1–4, 6 y 7**: importa el nuevo `.apkg` encima. Se conservan tu progreso y tus tarjetas; se agregan las nuevas y el submazo 08.

**Capítulo 5 (reparación del ADN)**: antes usaba tres tipos de nota propios (*RepADN · Cloze*, *RepADN · Pregunta-Respuesta* y *RepADN · Caso clínico*). Ahora sus 366 tarjetas son Basic, y Anki las importa como **notas nuevas**: no puede convertir una nota de un tipo a otro al importar. Las notas viejas siguen en tu colección hasta que las borres, así que tendrás las dos versiones. Elige una opción:

1. **Pasar a la versión Basic** (recomendado si llevas poco avance). En *Explorar*, busca

   ```
   note:"RepADN · Cloze" or note:"RepADN · Pregunta-Respuesta" or note:"RepADN · Caso clínico"
   ```

   selecciona todo (Ctrl+A o Cmd+A) y usa *Notas → Borrar*. Después borra los subdecks que quedan vacíos (*05 Reparación del ADN::00 · Fundamentos*, etc.) y, si quieres, los tres tipos de nota en *Herramientas → Administrar tipos de nota*. El progreso de esas tarjetas viejas se pierde; las nuevas empiezan desde cero.
2. **Conservar tu progreso en las viejas.** No borres nada y suspende las nuevas con la búsqueda `tag:reparacion note:"Genética Básico"` → *Tarjetas → Suspender*. Las tarjetas Basic del capítulo 5 que traen algo nuevo (la herencia de BRCA con penetrancia incompleta, la variante c.5946delT y la letalidad sintética del parcial) son `rep164`, `rep166b` y `rep235`: si quieres, reactívalas.

La misma búsqueda de la opción 1 encuentra también las notas del antiguo `Reparacion_ADN.apkg` (mazo *Reparación del ADN (Medicina)*), porque son las mismas.

## Editar o añadir tarjetas

Fuentes en la carpeta `anki/`: un archivo `cards_NN_tema.txt` por capítulo, con una nota Basic por línea.

```
id|sección|anverso|reverso|etiquetas
```

- `sección`: `01` a `08` (para una clase nueva, agrega la sección en `SECTIONS` y `TOPIC_TAG` dentro de `anki/build_deck.py`).
- No cambies el `id` de una nota existente; para notas nuevas usa un id nuevo.
- No uses `|` dentro del texto. Se admite HTML (`<b>`, `<i>`, `<div class=extra>`, `<div class=tema>` y las clases de `style.css`).

Regenerar el `.apkg`:

```bash
pip install --target ../.pylib -r anki/requirements.txt   # una sola vez, desde esta carpeta
python3 anki/build_deck.py
```

El script valida las fuentes (número de campos, ids duplicados, secciones, etiquetas HTML sin cerrar) antes de generar el archivo.
