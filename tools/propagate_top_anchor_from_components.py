#!/usr/bin/env python3
"""
Propagate missing 'top' anchors to composite base glyphs from their components.

For each glyph layer that lacks a 'top' anchor, if it has a component that
references a glyph (usually a base letter) which has a 'top' anchor on the
corresponding master layer, then copy that anchor position adjusted by the
component offset into the composite layer.

This is useful for composites like Aogonek/eogonek/etc. so they participate
in MarkToBase positioning for top combining marks.

Usage:
  python3 tools/propagate_top_anchor_from_components.py sources/Akt.glyphs
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

try:
    from glyphsLib import GSFont, GSAnchor, GSComponent
except Exception as e:
    print("[ERROR] glyphsLib is required. Install with: pip install glyphsLib")
    sys.exit(1)


def find_layer_for_master(glyph, master_id: str):
    for l in getattr(glyph, "layers", []) or []:
        if getattr(l, "layerId", None) == master_id:
            return l
    for l in getattr(glyph, "layers", []) or []:
        if getattr(l, "associatedMasterId", None) == master_id:
            return l
    return None


def get_anchor(layer, name: str) -> Optional[GSAnchor]:
    for a in getattr(layer, "anchors", []) or []:
        if getattr(a, "name", None) == name:
            return a
    return None


def ensure_anchor(layer, name: str, x: float, y: float) -> bool:
    if get_anchor(layer, name) is not None:
        return False
    a = GSAnchor()
    a.name = name
    try:
        a.position = (float(x), float(y))
    except Exception:
        try:
            a.x = float(x); a.y = float(y)
        except Exception:
            pass
    anchors = getattr(layer, "anchors", None)
    if anchors is None:
        layer.anchors = [a]
    else:
        anchors.append(a)
    return True


def component_offset(comp: GSComponent):
    # Try robustly to obtain component translation offset
    # GlyphsLib exposes .position or .transform depending on version
    try:
        pos = getattr(comp, "position", None)
        if pos is not None:
            try:
                return float(pos.x), float(pos.y)
            except Exception:
                if isinstance(pos, (tuple, list)) and len(pos) >= 2:
                    return float(pos[0]), float(pos[1])
    except Exception:
        pass
    try:
        # transform is (xx, xy, yx, yy, dx, dy)
        tr = getattr(comp, "transform", None)
        if tr and len(tr) >= 6:
            return float(tr[4]), float(tr[5])
    except Exception:
        pass
    try:
        x = float(getattr(comp, "x", 0.0))
        y = float(getattr(comp, "y", 0.0))
        return x, y
    except Exception:
        return 0.0, 0.0


def process(path: Path) -> int:
    font = GSFont(str(path))
    master_ids = [m.id for m in font.masters]
    created = 0

    # Map glyph name -> glyph object for quick reference
    glyph_map = {g.name: g for g in font.glyphs}

    for g in font.glyphs:
        for mid in master_ids:
            layer = find_layer_for_master(g, mid)
            if layer is None:
                continue
            # Skip if already has top
            if get_anchor(layer, "top") is not None:
                continue
            comps = getattr(layer, "components", None) or []
            if not comps:
                continue
            placed = False
            # Prefer first component that has a 'top' anchor on its own master layer
            for comp in comps:
                refname = getattr(comp, "name", None) or getattr(comp, "ref", None)
                if not refname:
                    continue
                ref_g = glyph_map.get(refname)
                if ref_g is None:
                    continue
                ref_layer = find_layer_for_master(ref_g, mid)
                if ref_layer is None:
                    continue
                a_top = get_anchor(ref_layer, "top")
                if a_top is None:
                    continue
                # Compute composite position by adding component offset
                dx, dy = component_offset(comp)
                try:
                    x0 = float(getattr(a_top, "x", getattr(a_top, "position", (0, 0))[0]))
                    y0 = float(getattr(a_top, "y", getattr(a_top, "position", (0, 0))[1]))
                except Exception:
                    continue
                if ensure_anchor(layer, "top", x0 + dx, y0 + dy):
                    created += 1
                    placed = True
                    break
            # If not placed from first relevant component, as a fallback try any component that has _top on mark (rare)
            if not placed:
                for comp in comps:
                    refname = getattr(comp, "name", None) or getattr(comp, "ref", None)
                    if not refname:
                        continue
                    ref_g = glyph_map.get(refname)
                    if ref_g is None:
                        continue
                    ref_layer = find_layer_for_master(ref_g, mid)
                    if ref_layer is None:
                        continue
                    a_t = get_anchor(ref_layer, "_top")
                    if a_t is None:
                        continue
                    dx, dy = component_offset(comp)
                    try:
                        x0 = float(getattr(a_t, "x", getattr(a_t, "position", (0, 0))[0]))
                        y0 = float(getattr(a_t, "y", getattr(a_t, "position", (0, 0))[1]))
                    except Exception:
                        continue
                    if ensure_anchor(layer, "top", x0 + dx, y0 + dy):
                        created += 1
                        break

    if created:
        font.save(str(path))
    print(f"[propagate_top_anchor_from_components] Anchors created: {created}")
    return created


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: propagate_top_anchor_from_components.py sources/Akt.glyphs")
        return 2
    p = Path(argv[1])
    if not p.exists():
        print(f"[ERROR] File not found: {p}")
        return 1
    process(p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))