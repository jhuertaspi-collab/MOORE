"""Genera el mazo único de Genética y Biología Molecular: Genetica_Biologia_Molecular.apkg.

Fuentes (en esta carpeta):
  cards_NN_tema.txt         -> notas Basic de las clases 01-04, 06 y 07
                               formato de cada línea:  id|sección|anverso|reverso|etiquetas
  cards_05_reparacion.json  -> notas de la clase 05 (reparación del ADN), con sus tres tipos de
                               nota propios (cloze, pregunta-respuesta y caso clínico)

Los ids (y los guid de la clase 05) son estables: si editas una nota conserva su id y Anki la
actualizará al reimportar sin perder el progreso.
Para añadir una clase nueva: agrega su sección en SECTIONS y TOPIC_TAG y crea cards_NN_tema.txt.
"""
import glob
import hashlib
import json
import os
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(OUT, "..", ".pylib"))
import genanki  # noqa: E402

ROOT = "Genética y Biología Molecular (UNAL 2026)"
SECTIONS = {
    "01": "01 Bioinformática y medicina genómica",
    "02": "02 Genética del desarrollo",
    "03": "03 Ciclo celular",
    "04": "04 Errores innatos del metabolismo",
    "05": "05 Reparación del ADN",
    "06": "06 Genética del cáncer",
    "07": "07 Técnicas de biología molecular",
}
TOPIC_TAG = {"01": "bioinformatica", "02": "desarrollo", "03": "ciclo_celular", "04": "eim",
             "05": "reparacion", "06": "cancer", "07": "tecnicas"}
REPAIR_JSON = os.path.join(HERE, "cards_05_reparacion.json")
CSS = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
CHECKED_TAGS = {"b", "i", "div", "sup", "sub", "code", "ul", "ol", "li"}


def stable_id(s):
    return int(hashlib.sha1(s.encode()).hexdigest()[:8], 16) + (1 << 30)


class TagBalance(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.errors = [], []

    def handle_starttag(self, tag, attrs):
        if tag in CHECKED_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in CHECKED_TAGS:
            if not self.stack or self.stack[-1] != tag:
                self.errors.append(f"cierre </{tag}> inesperado")
            else:
                self.stack.pop()


def check_html(text):
    p = TagBalance()
    p.feed(text)
    p.close()
    return p.errors + [f"<{t}> sin cerrar" for t in p.stack]


basic = genanki.Model(
    stable_id("genetica-basico-v1"), "Genética Básico",
    fields=[{"name": "Anverso"}, {"name": "Reverso"}], css=CSS,
    templates=[{"name": "Tarjeta",
                "qfmt": "<div class=q>{{Anverso}}</div>",
                "afmt": "<div class=q>{{Anverso}}</div><hr id=answer><div class=a>{{Reverso}}</div>"}])

decks = {}


def section_deck(sec):
    name = f"{ROOT}::{SECTIONS[sec]}"
    if name not in decks:
        # Mismo id que en las versiones anteriores del mazo (ROOT + número de sección).
        decks[name] = genanki.Deck(stable_id(ROOT + sec), name)
    return decks[name]


# --- Notas Basic (cards_*.txt) ---------------------------------------------------------------
rows, seen, problems = [], set(), []
for path in sorted(glob.glob(os.path.join(HERE, "cards_*.txt"))):
    name = os.path.basename(path)
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("|")
        if len(parts) != 5:
            problems.append(f"{name}:{n} tiene {len(parts)} campos (deben ser 5)")
            continue
        cid, sec, front, back, tags = parts
        if cid in seen:
            problems.append(f"{name}:{n} id duplicado {cid}")
        seen.add(cid)
        if sec not in SECTIONS or sec == "05":
            problems.append(f"{name}:{n} sección no válida {sec}")
            continue
        if not front.strip() or not back.strip():
            problems.append(f"{name}:{n} campo vacío")
        for label, text in (("anverso", front), ("reverso", back)):
            problems += [f"{name}:{n} {label}: {e}" for e in check_html(text)]
        rows.append((sec, cid, front, back, ["genetica", TOPIC_TAG[sec]] + tags.split()))

# --- Notas de reparación del ADN (cards_05_reparacion.json) -----------------------------------
repair = json.load(open(REPAIR_JSON, encoding="utf-8"))
models = {}
for m in repair["models"]:
    models[m["name"]] = genanki.Model(
        m["id"], m["name"], fields=[{"name": f} for f in m["fields"]],
        templates=m["templates"], css=m["css"], sort_field_index=m.get("sortf", 0),
        model_type=genanki.Model.CLOZE if m["type"] == 1 else genanki.Model.FRONT_BACK)
repair_notes = []
for i, note in enumerate(repair["notes"], 1):
    model = models.get(note["model"])
    if model is None:
        problems.append(f"cards_05_reparacion.json nota {i}: tipo de nota desconocido {note['model']}")
        continue
    if len(note["fields"]) != len(model.fields):
        problems.append(f"cards_05_reparacion.json nota {i}: {len(note['fields'])} campos (deben ser {len(model.fields)})")
        continue
    if note["guid"] in seen:
        problems.append(f"cards_05_reparacion.json nota {i}: guid duplicado {note['guid']}")
    seen.add(note["guid"])
    repair_notes.append(note)

if problems:
    sys.exit("Errores de formato:\n  " + "\n  ".join(problems))

rows.sort(key=lambda r: (r[0], r[1]))
for sec in SECTIONS:
    section_deck(sec)

for sec, cid, front, back, tags in rows:
    guid = "gb" + hashlib.sha1(cid.encode()).hexdigest()[:14]
    section_deck(sec).add_note(genanki.Note(model=basic, fields=[front, back], tags=tags, guid=guid))

for note in repair_notes:
    name = f"{ROOT}::{SECTIONS['05']}::{note['deck']}"
    if name not in decks:
        decks[name] = genanki.Deck(stable_id(name), name)
    tags = note["tags"] + [t for t in ("genetica", "reparacion") if t not in note["tags"]]
    decks[name].add_note(genanki.Note(model=models[note["model"]], fields=note["fields"], tags=tags, guid=note["guid"]))

genanki.Package(list(decks.values())).write_to_file(os.path.join(OUT, "Genetica_Biologia_Molecular.apkg"))
count = {SECTIONS[s]: len(repair_notes) if s == "05" else sum(r[0] == s for r in rows) for s in SECTIONS}
total_cards = len(rows) + sum(len(n.cards) for d in decks.values() for n in d.notes if n.model is not basic)
print(f"{len(rows) + len(repair_notes)} notas, {total_cards} tarjetas ->", count)
