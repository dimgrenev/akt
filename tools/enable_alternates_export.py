#!/usr/bin/env python3
import re
import sys
from pathlib import Path

try:
    from glyphsLib.classes import GSFont
except Exception as e:
    print(f"ERROR: glyphsLib not available: {e}")
    sys.exit(1)

SRC = Path(__file__).resolve().parents[1] / "sources" / "Akt.glyphs"

if not SRC.exists():
    print(f"ERROR: Source not found: {SRC}")
    sys.exit(1)

font = GSFont(str(SRC))

pattern = re.compile(r"\.(ss\d{2}|cv\d{2})($|\.)")
changed = 0
candidates = 0

for g in font.glyphs:
    name = getattr(g, "name", "") or ""
    if not name:
        continue
    if pattern.search(name):
        candidates += 1
        if getattr(g, "export", True) is False:
            g.export = True
            changed += 1

print(f"Candidates: {candidates}")
print(f"Enabled export for: {changed} glyphs")

font.save(str(SRC))
print("Saved:", SRC)