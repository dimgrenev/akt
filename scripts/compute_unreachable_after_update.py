#!/usr/bin/env python3
import re
from pathlib import Path
import unicodedata
import gfsubsets

root = Path(__file__).resolve().parents[1]
metadata = root / "fonts/METADATA.pb"
font_path = None
# find the variable TTF path from METADATA.pb filename field
if metadata.exists():
    txt = metadata.read_text(encoding="utf-8")
    m = re.search(r'filename:\s*"([^"]+)"', txt)
    if m:
        font_path = root / "fonts" / m.group(1)
    subsets = re.findall(r'subsets:\s*"([^"]+)"', txt)
else:
    raise SystemExit("METADATA.pb not found")

if not font_path or not font_path.exists():
    raise SystemExit(f"Font file not found: {font_path}")

# declared subsets set
declared = set(subsets)
# exclude 'menu' from coverage checks, since gfsubsets doesn't have it
if 'menu' in declared:
    declared.remove('menu')

cps = gfsubsets.CodepointsInFont(str(font_path))

uncovered = []
for cp in sorted(cps):
    subs = set(gfsubsets.SubsetsForCodepoint(cp))
    if not (subs & declared):
        # Not covered by any declared subset
        try:
            name = unicodedata.name(chr(cp))
        except ValueError:
            name = '<unnamed>'
        uncovered.append((cp, name, ','.join(sorted(subs)) or '<none>'))

out = root / "documentation/reports/unreachable_after_update.tsv"
with out.open("w", encoding="utf-8") as f:
    f.write("codepoint\tunicode_name\tall_matching_subsets\n")
    for cp, name, subs in uncovered:
        f.write(f"U+{cp:04X}\t{name}\t{subs}\n")

print(f"Declared subsets in METADATA.pb: {sorted(declared)}")
print(f"Uncovered codepoints after update: {len(uncovered)} -> {out}")