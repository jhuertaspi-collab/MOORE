"""Genera el mazo Anki (tipo Basic) de Genética y Biología Molecular desde cards_*.txt.

Salida (en la carpeta superior):
  Genetica_Biologia_Molecular.apkg   -> abrir con Anki
  genetica_biologia_molecular.txt    -> alternativa: Archivo > Importar (tipo de nota Basic)

Formato de cada línea de datos:  id|sección|anverso|reverso|etiquetas
El id es estable: si editas una tarjeta conserva su id y Anki la actualizará al reimportar.
Para añadir una clase nueva: agrega su sección en SECTIONS y crea cards_NN_tema.txt.
"""
import glob
import hashlib
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
}
TOPIC_TAG = {"01": "bioinformatica", "02": "desarrollo", "03": "ciclo_celular", "04": "eim"}
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
        if sec not in SECTIONS:
            problems.append(f"{name}:{n} sección desconocida {sec}")
            continue
        if not front.strip() or not back.strip():
            problems.append(f"{name}:{n} campo vacío")
        if front.lstrip().startswith('"') or back.lstrip().startswith('"'):
            problems.append(f"{name}:{n} un campo empieza con comillas dobles (rompe la importación .txt)")
        for label, text in (("anverso", front), ("reverso", back)):
            problems += [f"{name}:{n} {label}: {e}" for e in check_html(text)]
        rows.append((sec, cid, front, back, ["genetica", TOPIC_TAG[sec]] + tags.split()))

if problems:
    sys.exit("Errores de formato:\n  " + "\n  ".join(problems))

rows.sort(key=lambda r: (r[0], r[1]))
decks = {s: genanki.Deck(stable_id(ROOT + s), f"{ROOT}::{label}") for s, label in SECTIONS.items()}
with open(os.path.join(OUT, "genetica_biologia_molecular.txt"), "w", encoding="utf-8") as out:
    out.write("#separator:Pipe\n#html:true\n#guid column:1\n#notetype column:2\n#deck column:3\n#tags column:6\n")
    for sec, cid, front, back, tags in rows:
        guid = "gb" + hashlib.sha1(cid.encode()).hexdigest()[:14]
        decks[sec].add_note(genanki.Note(model=basic, fields=[front, back], tags=tags, guid=guid))
        out.write("|".join([guid, "Basic", decks[sec].name, front, back, " ".join(tags)]) + "\n")

genanki.Package(list(decks.values())).write_to_file(os.path.join(OUT, "Genetica_Biologia_Molecular.apkg"))
count = {SECTIONS[s]: sum(r[0] == s for r in rows) for s in SECTIONS}
print(f"{len(rows)} notas Basic ->", count)
