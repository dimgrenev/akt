#!/usr/bin/env python3
"""
Add missing 'top' anchors to composite base glyphs (like Aogonek, eogonek, ...)
by copying the 'top' anchor from their base component layer (e.g. A, a, E, e),
without considering ogonek components. This avoids shifting due to ogonek width
and places anchors precisely where combining top marks should attach.

Usage:
  python3 tools/add_top_anchors_from_base_component.py sources/Akt.glyphs Aogonek Eogonek Iogonek Uogonek aogonek aogonek.cv01 aogonek.ss01 aogonek.ss01.cv01 aogonek.ss02 aogonek.ss02.cv01 eogonek iogonek oogonek uogonek

The script is conservative: it ONLY adds 'top' if missing. It never adds other anchors.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, Optional, Tuple

try:
    from glyphsLib import GSFont, GSAnchor
except Exception:
    print("[ERROR] glyphsLib is required. Install with: pip install glyphsLib")
    sys.exit(1)


OGONEK_NAMES = {"ogonekcomb", "ogonek-mirrored"}


def find_layer_for_master(glyph, master_id):
    for l in glyph.layers:
        if getattr(l, "layerId", None) == master_id:
            return l
    for l in glyph.layers:
        if getattr(l, "associatedMasterId", None) == master_id:
            return l
    return None


def has_top(layer) -> bool:
    try:
        for a in getattr(layer, "anchors", []) or []:
            if a.name == "top":
                return True
    except Exception:
        pass
    return False


def get_top_from_layer(layer) -> Optional[Tuple[float, float]]:
    try:
        for a in getattr(layer, "anchors", []) or []:
            if a.name == "top":
                # glyphsLib supports .position or (x, y)
                try:
                    x, y = a.position
                except Exception:
                    x = float(getattr(a, "x", 0.0) or 0.0)
                    y = float(getattr(a, "y", 0.0) or 0.0)
                return (float(x), float(y))
    except Exception:
        pass
    return None


def add_top(layer, x: float, y: float) -> bool:
    if has_top(layer):
        return False
    a = GSAnchor()
    a.name = "top"
    try:
        a.position = (x, y)
    except Exception:
        try:
            a.x = x; a.y = y
        except Exception:
            pass
    anchors = getattr(layer, "anchors", None)
    if anchors is None:
        layer.anchors = [a]
    else:
        anchors.append(a)
    return True


def process(font_path: Path, glyph_names: Iterable[str]) -> None:
    font = GSFont(str(font_path))
    glyphs_map = {g.name: g for g in font.glyphs}
    created = 0
    for gname in glyph_names:
        g = glyphs_map.get(gname)
        if not g:
            print(f"[WARN] Glyph not found: {gname}")
            continue
        for m in font.masters:
            layer = find_layer_for_master(g, m.id)
            if not layer:
                print(f"[WARN] No layer for glyph {gname} in master {m.name}")
                continue
            if has_top(layer):
                continue
            # find base component (first component that is not ogonek)
            base_ref_name: Optional[str] = None
            for comp in getattr(layer, "components", []) or []:
                name = getattr(comp, "name", None) or getattr(comp, "componentName", None) or getattr(comp, "ref", None)
                if not name:
                    continue
                # normalize ref string
                refname = str(name)
                if any(x in refname for x in OGONEK_NAMES):
                    continue
                base_ref_name = refname
                break
            # If components API not populated (using shapes), fall back to shapes
            if not base_ref_name:
                for shp in getattr(layer, "shapes", []) or []:
                    name = getattr(shp, "name", None) or getattr(shp, "componentName", None) or getattr(shp, "ref", None)
                    if not name:
                        continue
                    refname = str(name)
                    if any(x in refname for x in OGONEK_NAMES):
                        continue
                    base_ref_name = refname
                    break
            if not base_ref_name:
                print(f"[WARN] Could not determine base component for {gname} in {m.name}")
                continue
            base_glyph = glyphs_map.get(base_ref_name)
            if not base_glyph:
                print(f"[WARN] Base glyph '{base_ref_name}' not found for {gname}")
                continue
            base_layer = find_layer_for_master(base_glyph, m.id)
            if not base_layer:
                print(f"[WARN] No base layer for {base_ref_name} in master {m.name}")
                continue
            top = get_top_from_layer(base_layer)
            if top is None:
                # Fallback to base bounds
                try:
                    b = base_layer.bounds
                    min_x = float(getattr(b.origin, "x", 0.0))
                    max_x = min_x + float(getattr(b.size, "width", 0.0))
                    max_y = float(getattr(b.origin, "y", 0.0)) + float(getattr(b.size, "height", 0.0))
                    cx = (min_x + max_x) * 0.5
                    top = (cx, max_y)
                except Exception:
                    print(f"[WARN] Could not compute bounds for base {base_ref_name} in {m.name}")
                    continue
            if add_top(layer, *top):
                created += 1
    if created:
        font.save(str(font_path))
    print(f"Top anchors created (from base): {created}")


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: add_top_anchors_from_base_component.py <font.glyphs> <glyphname> [glyphname ...]")
        return 2
    font_path = Path(argv[1])
    if not font_path.exists():
        print(f"[ERROR] File not found: {font_path}")
        return 1
    names = argv[2:]
    process(font_path, names)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))