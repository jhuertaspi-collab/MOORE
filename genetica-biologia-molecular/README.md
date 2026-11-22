# Genética y Biología Molecular (Medicina UNAL, 2026)

Guía de estudio y mazo de Anki (tipo **Basic**) construidos a partir de las diapositivas de clase, con los datos verificados contra fuentes primarias.

**Empieza aquí: [Guía de estudio](Guia_de_estudio.md)** (índice, conexiones entre clases, tabla de enfermedades y fe de erratas).

| # | Clase | Guía | Tarjetas |
|---|---|---|---|
| 1 | Introducción a la bioinformática y medicina genómica | [guía](guia/01_Bioinformatica_y_medicina_genomica.md) | 66 |
| 2 | Genética del desarrollo | [guía](guia/02_Genetica_del_desarrollo.md) | 84 |
| 3 | Ciclo celular | [guía](guia/03_Ciclo_celular.md) | 125 |
| 4 | Errores innatos del metabolismo | [guía](guia/04_Errores_innatos_del_metabolismo.md) | 108 |
| | **Total** | | **383** |

La clase de reparación del ADN tiene su guía y su mazo en [`../reparacion-adn`](../reparacion-adn/).

## Importar el mazo

- **Recomendado:** descarga [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg) y ábrelo con Anki (escritorio, AnkiDroid o AnkiMobile). Crea el mazo *Genética y Biología Molecular (UNAL 2026)* con un submazo por clase, el tipo de nota *Genética Básico* (dos campos, una tarjeta por nota, igual que Basic) y diseño con modo nocturno.
- **Alternativa:** [`genetica_biologia_molecular.txt`](genetica_biologia_molecular.txt) con *Archivo → Importar* (Anki 2.1.55 o posterior). Usa el tipo de nota estándar **Basic**.

Usa solo uno de los dos archivos. Cada nota tiene un id fijo: al reimportar una versión nueva, Anki actualiza las notas existentes y agrega las nuevas sin duplicar ni borrar tu progreso.

## Editar o añadir tarjetas

Las tarjetas están en `anki/cards_*.txt`, una nota por línea:

```
id|sección|anverso|reverso|etiquetas
```

- `sección`: `01` a `04` (para una clase nueva, agrega la sección en `SECTIONS` dentro de `anki/build_deck.py`).
- No cambies el `id` de una nota existente; para notas nuevas usa un id nuevo.
- No uses `|` dentro del texto. Se admite HTML (`<b>`, `<i>`, `<div class=extra>`).

Regenerar el `.apkg` y el `.txt`:

```bash
pip install --target ../.pylib -r anki/requirements.txt   # una sola vez, desde esta carpeta
python3 anki/build_deck.py
```

El script valida cada línea (número de campos, ids duplicados, secciones, etiquetas HTML sin cerrar) antes de generar los archivos.
