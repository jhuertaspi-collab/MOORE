# Genética y Biología Molecular (Medicina UNAL, 2026)

Guía de estudio y mazos de Anki construidos a partir de las diapositivas de clase, con los datos verificados contra fuentes primarias.

**Empieza aquí: [Guía de estudio](Guia_de_estudio.md)** (índice, conexiones entre clases, tabla de enfermedades y fe de erratas).

| # | Clase | Guía | Mazo | Tarjetas |
|---|---|---|---|---|
| 1 | Introducción a la bioinformática y medicina genómica | [guía](guia/01_Bioinformatica_y_medicina_genomica.md) | `Genetica_Biologia_Molecular.apkg` | 66 |
| 2 | Genética del desarrollo | [guía](guia/02_Genetica_del_desarrollo.md) | `Genetica_Biologia_Molecular.apkg` | 84 |
| 3 | Ciclo celular | [guía](guia/03_Ciclo_celular.md) | `Genetica_Biologia_Molecular.apkg` | 125 |
| 4 | Errores innatos del metabolismo | [guía](guia/04_Errores_innatos_del_metabolismo.md) | `Genetica_Biologia_Molecular.apkg` | 108 |
| 5 | Mecanismos de reparación del ADN | [guía](guia/05_Reparacion_del_ADN.md) | `Reparacion_ADN.apkg` | 366 |
| 6 | Genética del cáncer: hallmarks y perspectivas terapéuticas | [guía](guia/06_Genetica_del_cancer.md) | `Genetica_Biologia_Molecular.apkg` | 156 |
| 7 | Técnicas de biología molecular | [guía](guia/07_Tecnicas_de_biologia_molecular.md) | `Genetica_Biologia_Molecular.apkg` | 142 |

El mazo Basic suma **681 tarjetas** (clases 1–4, 6 y 7).

## Importar el mazo de reparación del ADN

Descarga [`Reparacion_ADN.apkg`](Reparacion_ADN.apkg) y ábrelo con Anki. Crea el mazo *Reparación del ADN (Medicina)* con tarjetas de pregunta-respuesta, cloze y casos clínicos. Si ya lo habías importado desde la carpeta anterior (`reparacion-adn/`), es el mismo archivo: no hace falta volver a importarlo.

## Importar el mazo Basic (clases 1–4, 6 y 7)

- **Recomendado:** descarga [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg) y ábrelo con Anki (escritorio, AnkiDroid o AnkiMobile). Crea el mazo *Genética y Biología Molecular (UNAL 2026)* con un submazo por clase, el tipo de nota *Genética Básico* (dos campos, una tarjeta por nota, igual que Basic) y diseño con modo nocturno.
- **Alternativa:** [`genetica_biologia_molecular.txt`](genetica_biologia_molecular.txt) con *Archivo → Importar* (Anki 2.1.55 o posterior). Usa el tipo de nota estándar **Basic**.

Usa solo uno de los dos archivos. Cada nota tiene un id fijo: al reimportar una versión nueva, Anki actualiza las notas existentes y agrega las nuevas sin duplicar ni borrar tu progreso. Si ya habías importado la versión anterior (383 tarjetas), importa el `.apkg` nuevo encima: se agregan los submazos 06 y 07.

## Editar o añadir tarjetas

Las tarjetas están en `anki/cards_*.txt`, una nota por línea:

```
id|sección|anverso|reverso|etiquetas
```

- `sección`: `01`–`04`, `06` o `07` (para una clase nueva, agrega la sección en `SECTIONS` dentro de `anki/build_deck.py`).
- No cambies el `id` de una nota existente; para notas nuevas usa un id nuevo.
- No uses `|` dentro del texto. Se admite HTML (`<b>`, `<i>`, `<div class=extra>`).

Regenerar el `.apkg` y el `.txt`:

```bash
pip install --target ../.pylib -r anki/requirements.txt   # una sola vez, desde esta carpeta
python3 anki/build_deck.py
```

El script valida cada línea (número de campos, ids duplicados, secciones, etiquetas HTML sin cerrar) antes de generar los archivos.
