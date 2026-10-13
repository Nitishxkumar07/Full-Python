"""07 - Files, paths, json, csv."""
import csv
import json
import tempfile
from pathlib import Path

tmp = Path(tempfile.mkdtemp())

# --- Text files: always use `with` and explicit encoding ---
p = tmp / "notes.txt"
p.write_text("line1\nline2\n", encoding="utf-8")
with p.open(encoding="utf-8") as fh:
    for line in fh:                      # lazy, memory friendly
        print(line.rstrip())
with p.open("a", encoding="utf-8") as fh:
    fh.write("line3\n")
print(p.read_text(encoding="utf-8").splitlines())

# --- pathlib ---
print(p.name, p.stem, p.suffix, p.parent == tmp, p.exists())
for f in tmp.glob("*.txt"):
    print("found", f.name)

# --- JSON ---
data = {"name": "Ada", "langs": ["py", "c"]}
jp = tmp / "data.json"
jp.write_text(json.dumps(data, indent=2))
print(json.loads(jp.read_text()))

# --- CSV ---
cp = tmp / "people.csv"
with cp.open("w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["name", "age"])
    w.writeheader(); w.writerow({"name": "Ada", "age": 36})
with cp.open(newline="", encoding="utf-8") as fh:
    print(list(csv.DictReader(fh)))
