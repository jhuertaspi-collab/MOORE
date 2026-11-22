# Genética y Biología Molecular (Medicina UNAL, 2026)

Una guía de estudio y un mazo de Anki, construidos a partir de las diapositivas de clase, con los datos verificados contra fuentes primarias.

| Archivo | Qué es |
|---|---|
| [`Guia_de_estudio.md`](Guia_de_estudio.md) | **La guía completa**: los 7 capítulos en un solo archivo, con índice general, conexiones entre clases, tabla de enfermedades y fe de erratas |
| [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg) | **El mazo completo**: 1.047 tarjetas, un submazo por capítulo |

| # | Clase | Capítulo en la guía | Tarjetas |
|---|---|---|---|
| 1 | Introducción a la bioinformática y medicina genómica | [capítulo 1](Guia_de_estudio.md#1-introducción-a-la-bioinformática-y-medicina-genómica) | 66 |
| 2 | Genética del desarrollo | [capítulo 2](Guia_de_estudio.md#2-genética-del-desarrollo) | 84 |
| 3 | Ciclo celular | [capítulo 3](Guia_de_estudio.md#3-ciclo-celular-fases-motor-molecular-y-puntos-de-control) | 125 |
| 4 | Errores innatos del metabolismo | [capítulo 4](Guia_de_estudio.md#4-errores-innatos-del-metabolismo-eim) | 108 |
| 5 | Mecanismos de reparación del ADN | [capítulo 5](Guia_de_estudio.md#5-mecanismos-de-reparación-del-adn-de-la-lesión-molecular-a-la-clínica) | 366 |
| 6 | Genética del cáncer: hallmarks y perspectivas terapéuticas | [capítulo 6](Guia_de_estudio.md#6-genética-del-cáncer-biología-molecular-hallmarks-y-perspectivas-terapéuticas) | 156 |
| 7 | Técnicas de biología molecular | [capítulo 7](Guia_de_estudio.md#7-técnicas-de-biología-molecular) | 142 |
| | **Total** | | **1.047** |

## Importar el mazo

Descarga [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg) y ábrelo con Anki (escritorio, AnkiDroid o AnkiMobile). Crea el mazo *Genética y Biología Molecular (UNAL 2026)* con los submazos 01 a 07.

- Capítulos 1–4, 6 y 7: tipo de nota *Genética Básico* (dos campos, una tarjeta por nota, igual que Basic), con modo nocturno.
- Capítulo 5: conserva sus tres tipos de nota (*RepADN · Cloze*, *RepADN · Pregunta-Respuesta* y *RepADN · Caso clínico*) y sus 11 subdecks.

Cada nota tiene un id fijo: al reimportar una versión nueva, Anki actualiza las notas existentes y agrega las nuevas **sin duplicar ni borrar tu progreso**.

**Si ya habías importado alguna versión anterior:**

- `Genetica_Biologia_Molecular.apkg` (383 o 681 tarjetas): importa el nuevo encima. Se agregan los submazos que faltan.
- `Reparacion_ADN.apkg`: sus notas ya están en tu colección y Anki no las duplica, pero sus tarjetas se quedan en el mazo viejo *Reparación del ADN (Medicina)*. Para tener todo junto, en *Explorar* selecciona ese mazo y usa *Tarjetas → Cambiar mazo* para moverlas a *05 Reparación del ADN*, o simplemente sigue estudiándolas donde están. El progreso se conserva en ambos casos.

## Editar o añadir tarjetas

Fuentes en la carpeta `anki/`:

- `cards_NN_tema.txt` (capítulos 1–4, 6 y 7): una nota Basic por línea.

  ```
  id|sección|anverso|reverso|etiquetas
  ```

  - `sección`: `01`–`04`, `06` o `07` (para una clase nueva, agrega la sección en `SECTIONS` y `TOPIC_TAG` dentro de `anki/build_deck.py`).
  - No cambies el `id` de una nota existente; para notas nuevas usa un id nuevo.
  - No uses `|` dentro del texto. Se admite HTML (`<b>`, `<i>`, `<div class=extra>`).
- `cards_05_reparacion.json` (capítulo 5): los tres tipos de nota y sus 234 notas, con su `guid`, sus campos, etiquetas y subdeck. No cambies los `guid`.

Regenerar el `.apkg`:

```bash
pip install --target ../.pylib -r anki/requirements.txt   # una sola vez, desde esta carpeta
python3 anki/build_deck.py
```

El script valida las fuentes (número de campos, ids duplicados, secciones, etiquetas HTML sin cerrar) antes de generar el archivo.
