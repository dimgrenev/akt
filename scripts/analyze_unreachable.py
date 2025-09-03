#!/usr/bin/env python3
import json
from pathlib import Path
import unicodedata

root = Path(__file__).resolve().parents[1]
src = root / "documentation/reports/unreachable_codepoints.json"
out_dir = root / "documentation/reports"
out_dir.mkdir(parents=True, exist_ok=True)

if not src.exists():
    raise SystemExit(f"ERROR: {src} not found")

data = json.loads(src.read_text(encoding="utf-8"))

# Expecting list of objects with keys: cp, name, suggested_subsets
if not isinstance(data, list) or not data or "cp" not in data[0]:
    raise SystemExit("Unexpected JSON structure in unreachable_codepoints.json")

all_items = data
with_ms = [it for it in all_items if any(s in (it.get("suggested_subsets") or []) for s in ("math","symbols"))]
without_ms = [it for it in all_items if not any(s in (it.get("suggested_subsets") or []) for s in ("math","symbols"))]

# Helper to write TSV

def write_tsv(path: Path, items):
    with path.open("w", encoding="utf-8") as f:
        f.write("codepoint\tunicode_name\tsuggested_subsets\n")
        for it in items:
            cp = it.get("cp") or ""
            name = it.get("name") or ""
            sugg = it.get("suggested_subsets") or []
            f.write(f"{cp}\t{name}\t{','.join(sugg)}\n")

write_tsv(out_dir/"unreachable_all.tsv", all_items)
write_tsv(out_dir/"unreachable_covered_by_math_or_symbols.tsv", with_ms)
write_tsv(out_dir/"unreachable_remaining_after_math_symbols.tsv", without_ms)

print("Generated:")
print(" -", (out_dir/"unreachable_all.tsv").as_posix(), len(all_items), "rows")
print(" -", (out_dir/"unreachable_covered_by_math_or_symbols.tsv").as_posix(), len(with_ms), "rows")
print(" -", (out_dir/"unreachable_remaining_after_math_symbols.tsv").as_posix(), len(without_ms), "rows")