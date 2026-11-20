# Moore 9e · Capítulo 6: Pelvis y periné (Anki)

323 notas → 738 tarjetas de repaso, en 10 submazos:

| Submazo | Notas |
|---|---|
| 01 Pelvis ósea y articulaciones | 32 |
| 02 Paredes, piso, peritoneo y fascia | 26 |
| 03 Neurovascular | 45 |
| 04 Órganos urinarios y recto | 38 |
| 05 Genitales internos masculinos | 20 |
| 06 Genitales internos femeninos | 43 |
| 07 Periné y triángulo anal | 38 |
| 08 Triángulo urogenital masculino | 25 |
| 09 Triángulo urogenital femenino | 26 |
| 10 Casos clínicos integrados | 30 |

## Importar

- **Recomendado:** descarga `Moore_Cap6_Pelvis_Perine.apkg` y ábrelo con Anki (escritorio, AnkiDroid o AnkiMobile). Trae su propio diseño con modo nocturno.
- **Alternativa:** `moore_cap6_pelvis_perine.txt` con *Archivo → Importar* (Anki 2.1.55+). Usa los tipos de nota estándar Basic y Cloze.

Usa solo uno de los dos archivos. Cada nota tiene un id fijo: al reimportar una versión corregida, Anki actualiza las notas en lugar de duplicarlas.

Etiquetas útiles para filtrar: `clinica`, `caso`, `dolor`, `linfa`, `homologias`, `anestesia`, `sexo`, `pectinea`.

## Editar o añadir tarjetas

Las tarjetas viven en `cards_*.txt`, una nota por línea:

```
id|tipo|sección|campo1|campo2|etiquetas
```

- `tipo`: `B` (básica: anverso/reverso) o `C` (cloze: texto/extra).
- `sección`: `01` a `10`.
- No cambies el `id` de una nota existente; para notas nuevas usa un id nuevo.
- No uses `|` dentro del texto.

Después regenera el `.apkg` y el `.txt`:

```bash
pip install -r requirements.txt
python3 build_deck.py
```

El script valida el formato (número de campos, ids duplicados, cloze mal cerradas) antes de generar los archivos.

## Nota de contenido

La traducción del Moore atribuye el útero bicorne a los conductos «mesonéfricos»; la tarjeta usa el término correcto, **paramesonéfricos (de Müller)**.
