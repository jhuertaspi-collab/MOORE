"""Genera el mazo Anki (Moore cap. 6) desde cards_*.txt -> .apkg y .txt importable.
Formato de cada línea de datos:  id|B o C|sección|campo1|campo2|etiquetas
El id es estable: si editas una tarjeta conserva su id y Anki la actualizará al reimportar."""
import glob, os, sys, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".pylib"))
import genanki

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "Moore::Cap6 Pelvis y Periné"
SECTIONS = {
    "01": "01 Pelvis ósea y articulaciones", "02": "02 Paredes, piso, peritoneo y fascia",
    "03": "03 Neurovascular", "04": "04 Órganos urinarios y recto",
    "05": "05 Genitales internos masculinos", "06": "06 Genitales internos femeninos",
    "07": "07 Periné y triángulo anal", "08": "08 Triángulo urogenital masculino",
    "09": "09 Triángulo urogenital femenino", "10": "10 Casos clínicos integrados",
}
CSS = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()

def stable_id(s):  # id numérico estable para mazos/modelos
    return int(hashlib.sha1(s.encode()).hexdigest()[:8], 16) + (1 << 30)

basic = genanki.Model(stable_id("moore-basico-v1"), "Moore Básico",
    fields=[{"name": "Anverso"}, {"name": "Reverso"}], css=CSS,
    templates=[{"name": "Tarjeta", "qfmt": "<div class=q>{{Anverso}}</div>",
                "afmt": "<div class=q>{{Anverso}}</div><hr id=answer><div class=a>{{Reverso}}</div>"}])
cloze = genanki.Model(stable_id("moore-cloze-v1"), "Moore Cloze", model_type=genanki.Model.CLOZE,
    fields=[{"name": "Texto"}, {"name": "Extra"}], css=CSS,
    templates=[{"name": "Cloze", "qfmt": "{{cloze:Texto}}",
                "afmt": "{{cloze:Texto}}{{#Extra}}<div class=extra>{{Extra}}</div>{{/Extra}}"}])

rows, seen = [], set()
for path in sorted(glob.glob(os.path.join(HERE, "cards_*.txt"))):
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("|")
        assert len(parts) == 6, f"{path}:{n} tiene {len(parts)} campos"
        cid, kind, sec, f1, f2, tags = parts
        assert cid not in seen, f"id duplicado {cid}"; seen.add(cid)
        assert kind in "BC" and sec in SECTIONS, f"{path}:{n} tipo/sección inválidos"
        if kind == "C":
            assert "{{c" in f1 and f1.count("{{") == f1.count("}}"), f"{path}:{n} cloze mal formada"
        rows.append((cid, kind, sec, f1, f2, ["moore", "cap6"] + tags.split()))

decks = {s: genanki.Deck(stable_id(ROOT + s), f"{ROOT}::{name}") for s, name in SECTIONS.items()}
with open(os.path.join(HERE, "moore_cap6_pelvis_perine.txt"), "w", encoding="utf-8") as out:
    out.write("#separator:Pipe\n#html:true\n#guid column:1\n#notetype column:2\n#deck column:3\n#tags column:6\n")
    for cid, kind, sec, f1, f2, tags in rows:
        guid = "m6" + hashlib.sha1(cid.encode()).hexdigest()[:14]  # hex: sin '|' ni '#'
        model = basic if kind == "B" else cloze
        decks[sec].add_note(genanki.Note(model=model, fields=[f1, f2], tags=tags, guid=guid))
        out.write("|".join([guid, "Basic" if kind == "B" else "Cloze", decks[sec].name, f1, f2, " ".join(tags)]) + "\n")
genanki.Package(list(decks.values())).write_to_file(os.path.join(HERE, "Moore_Cap6_Pelvis_Perine.apkg"))
count = {s: sum(r[2] == s for r in rows) for s in SECTIONS}
print(f"{len(rows)} notas ->", count)
