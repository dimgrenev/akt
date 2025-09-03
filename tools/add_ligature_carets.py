#!/usr/bin/env python3
"""
Add missing ligature caret anchors (caret_1, caret_2, ...) to specified ligature glyphs
across all masters in a Glyphs source.

Heuristic placement:
- If the layer has components, sort them left-to-right by their bounds and place carets
  midway between adjacent component bounds (average of right edge of left component and
  left edge of right component).
- If the layer has no components, fall back to evenly spaced positions across the advance width:
  for 2-part ligatures: 50% of width; for 3-part: ~33% and ~66%.

Usage:
  python3 tools/add_ligature_carets.py sources/Akt.glyphs [glyphname ...]
If no glyph list is provided, a sensible default list is used based on project GSUB:
  f_j f_t f_f_j I_J Ldot ldot numero
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, List, Tuple, Optional

try:
    from glyphsLib import GSFont, GSAnchor
except Exception:
    print("[ERROR] glyphsLib is required. Install with: pip install glyphsLib")
    sys.exit(1)


DEFAULT_LIGATURES = [
    "f_j",
    "f_t",
    "f_f_j",
    "I_J",
    "Ldot",
    "ldot",
    "numero",  # U+2116
    # Common f-ligatures present in GSUB
    "fi",
    "fl",
    "f_f",
    "f_f_i",
    "f_f_l",
]


def get_layer_for_master(glyph, master) -> object | None:
    # prefer layerId match, fall back to associatedMasterId
    for l in glyph.layers:
        if getattr(l, "layerId", None) == master.id:
            return l
    for l in glyph.layers:
        if getattr(l, "associatedMasterId", None) == master.id:
            return l
    return None


def bounds_of_component(layer, comp) -> Tuple[float, float, float, float]:
    try:
        b = comp.bounds
        min_x = float(getattr(b.origin, "x", 0.0))
        min_y = float(getattr(b.origin, "y", 0.0))
        max_x = min_x + float(getattr(b.size, "width", 0.0))
        max_y = min_y + float(getattr(b.size, "height", 0.0))
        return min_x, min_y, max_x, max_y
    except Exception:
        # Fallback to layer bounds if component bounds are not available
        try:
            b = layer.bounds
            min_x = float(getattr(b.origin, "x", 0.0))
            min_y = float(getattr(b.origin, "y", 0.0))
            max_x = min_x + float(getattr(b.size, "width", 0.0))
            max_y = min_y + float(getattr(b.size, "height", 0.0))
            return min_x, min_y, max_x, max_y
        except Exception:
            w = float(getattr(layer, "width", 0.0) or 0.0)
            return 0.0, 0.0, w, 0.0


def layer_bounds(layer) -> Tuple[float, float, float, float]:
    try:
        b = layer.bounds
        min_x = float(getattr(b.origin, "x", 0.0))
        min_y = float(getattr(b.origin, "y", 0.0))
        max_x = min_x + float(getattr(b.size, "width", 0.0))
        max_y = min_y + float(getattr(b.size, "height", 0.0))
        return min_x, min_y, max_x, max_y
    except Exception:
        w = float(getattr(layer, "width", 0.0) or 0.0)
        return 0.0, 0.0, w, 0.0


def existing_caret_names(layer) -> set[str]:
    names = set()
    try:
        for a in getattr(layer, "anchors", []) or []:
            n = getattr(a, "name", "") or ""
            if n == "caret" or n.startswith("caret_"):
                names.add(n)
    except Exception:
        pass
    return names


def ensure_anchor(layer, name: str, x: float, y: float) -> bool:
    # Don't duplicate existent anchors with the same name
    for a in getattr(layer, "anchors", []) or []:
        if getattr(a, "name", "") == name:
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


def compute_caret_positions(layer, desired_count: int) -> List[float]:
    # Try to use component boundaries
    comps = list(getattr(layer, "components", []) or [])
    if comps:
        # Build a simple left-to-right order by component minX
        comp_bounds = [(bounds_of_component(layer, c), c) for c in comps]
        comp_bounds.sort(key=lambda item: item[0][0])
        # Generate split positions between adjacent components
        xs: List[float] = []
        for i in range(len(comp_bounds) - 1):
            left_max_x = comp_bounds[i][0][2]
            right_min_x = comp_bounds[i + 1][0][0]
            xs.append((left_max_x + right_min_x) * 0.5)
        if xs:
            # Trim or pad to desired_count if needed
            if len(xs) >= desired_count:
                return xs[:desired_count]
            # If fewer boundaries than desired (rare), pad using width fractions
            min_x, _, max_x, _ = layer_bounds(layer)
            w = max(0.0, max_x - min_x)
            while len(xs) < desired_count:
                xs.append(min_x + w * (len(xs) + 1) / (desired_count + 1))
            return xs
    # Fallback: evenly spaced across advance width
    min_x, _, max_x, _ = layer_bounds(layer)
    w = max(0.0, max_x - min_x)
    return [min_x + w * (i + 1) / (desired_count + 1) for i in range(desired_count)]


def resolve_glyph(font: GSFont, name: str):
    # Direct name first
    for g in font.glyphs:
        if getattr(g, "name", None) == name:
            return g
    # If name looks like uniXXXX, try resolve by unicode
    if name.startswith("uni") and len(name) == 7:
        try:
            cp = int(name[3:], 16)
            hexd = f"{cp:04X}"
            for g in font.glyphs:
                # Glyphs can have .unicode or .unicodes
                u = getattr(g, "unicode", None)
                if u and u.upper() == hexd:
                    return g
                us = getattr(g, "unicodes", None) or []
                for uu in us:
                    if str(uu).upper() == hexd:
                        return g
        except Exception:
            pass
    # Some common aliases
    aliases = {
        "uni2116": "numero",
    }
    alias = aliases.get(name)
    if alias:
        for g in font.glyphs:
            if getattr(g, "name", None) == alias:
                return g
    return None


def desired_caret_count_for_layer(layer) -> int:
    comps = list(getattr(layer, "components", []) or [])
    if len(comps) >= 2:
        return len(comps) - 1
    # fallback for shapes drawn without components but still lig-like
    min_x, _, max_x, _ = layer_bounds(layer)
    return 1 if (max_x - min_x) > 0 else 0


def process(font_path: Path, glyph_names: Iterable[str]) -> int:
    font = GSFont(str(font_path))
    total_created = 0

    for gname in glyph_names:
        g = resolve_glyph(font, gname)
        if not g:
            print(f"[WARN] Glyph not found: {gname}")
            continue
        for m in font.masters:
            layer = get_layer_for_master(g, m)
            if not layer:
                print(f"[WARN] No layer for glyph {getattr(g, 'name', gname)} in master {m.name}")
                continue
            desired_count = desired_caret_count_for_layer(layer)
            if desired_count <= 0:
                continue
            # Skip layers that already have the desired number of carets
            existing = sorted([n for n in existing_caret_names(layer)])
            if len(existing) >= desired_count:
                continue
            # Compute positions and add missing carets in order
            xs = compute_caret_positions(layer, desired_count)
            y = 0.0
            created_here = 0
            for idx in range(desired_count):
                name = f"caret_{idx+1}"
                if name in existing:
                    continue
                if ensure_anchor(layer, name, xs[idx], y):
                    created_here += 1
            total_created += created_here
    if total_created:
        font.save(str(font_path))
    print(f"Ligature caret anchors created: {total_created}")
    return total_created


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: add_ligature_carets.py <font.glyphs> [glyphname ...]")
        return 2
    font_path = Path(argv[1])
    if not font_path.exists():
        print(f"[ERROR] File not found: {font_path}")
        return 1
    names = argv[2:] if len(argv) > 2 else DEFAULT_LIGATURES
    if not names:
        names = DEFAULT_LIGATURES
    process(font_path, names)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))