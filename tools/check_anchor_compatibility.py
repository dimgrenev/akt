#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check anchor name compatibility across masters in a Glyphs source.
Reports glyphs whose anchor name sets differ between masters, focusing on
mark attachment anchors: top/bottom on base glyphs and _top/_bottom on combining marks.

Usage:
  python3 tools/check_anchor_compatibility.py sources/Akt.glyphs
"""
import sys
from collections import defaultdict

try:
    import glyphsLib
except Exception as e:
    print("ERROR: glyphsLib is required:", e)
    sys.exit(1)


def main(path: str) -> int:
    font = glyphsLib.GSFont(path)
    masters = list(font.masters)
    master_ids = [m.id for m in masters]
    master_names = [m.name for m in masters]

    incompatible = []
    missing_by_master = defaultdict(lambda: defaultdict(set))

    for g in font.glyphs:
        # Determine category: 'Letter' vs 'Mark' (combining marks)
        cat = g.category or ""
        is_mark = (cat == "Mark")
        is_letter = (cat == "Letter")

        # We only care about these anchors primarily
        interesting = {"top", "bottom", "_top", "_bottom"}

        per_master = []
        for mid in master_ids:
            layer = g.layers[mid]
            names = set(a.name for a in (layer.anchors or []))
            if interesting & names:
                names = {n for n in names if n in interesting}
            per_master.append(names)

        # If all sets equal, skip
        if all(s == per_master[0] for s in per_master[1:]):
            continue

        # For marks, require underscore anchors be consistent.
        # For letters, require non-underscore anchors be consistent.
        union = set().union(*per_master)
        if is_mark:
            relevant = {n for n in union if n.startswith("_")}
        elif is_letter:
            relevant = {n for n in union if not n.startswith("_")}
        else:
            # ignore non-letter non-mark
            continue

        # If relevant empty, skip
        if not relevant:
            continue

        # Compute per-master missing relevant anchors
        for i, names in enumerate(per_master):
            missing = relevant - names
            if missing:
                missing_by_master[master_names[i]][g.name].update(sorted(missing))

        incompatible.append(g.name)

    # Print summary
    total = len(incompatible)
    print(f"Masters: {', '.join(master_names)}")
    print(f"Total glyphs with incompatible anchor sets: {total}")
    for mname, issues in missing_by_master.items():
        if not issues:
            continue
        print(f"\n== Master: {mname} ==")
        for gname in sorted(issues.keys()):
            miss = ", ".join(sorted(issues[gname]))
            print(f"  {gname}: missing {miss}")

    if total == 0:
        print("All good: anchor sets are consistent across masters for relevant glyphs.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tools/check_anchor_compatibility.py sources/Akt.glyphs")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))