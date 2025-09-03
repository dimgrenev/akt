#!/usr/bin/env python3
"""
Normalize anchors of combining diacritics in a .glyphs source.

Goals:
- Ensure each combining mark has only the relevant pair of anchors:
  * top marks:    _top + top
  * bottom marks: _bottom + bottom
  * ogonek mark:  _ogonek + ogonek
  * overlay marks: _center + center
- Place anchors at logical positions derived from the glyph's outline bbox per master:
  * top marks:    _top at (centerX, minY), top at (centerX, maxY)
  * bottom marks: _bottom at (centerX, maxY), bottom at (centerX, minY)
  * overlay:      both at geometric center (centerX, centerY)
  * ogonek:       _ogonek at (centerX, maxY), ogonek at (centerX, minY)
- Leave non-mark glyphs untouched. Does not edit side anchors (e.g. right/_right).

Usage:
  python3 tools/normalize_mark_anchors.py sources/Akt.glyphs

Notes:
- This tool computes layer bounds using paths and components (translated/scaled; rotation/skew are ignored if present).
- For component bounds, it attempts to use the referenced glyph's corresponding master layer.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple

try:
    from glyphsLib import GSFont, GSAnchor, GSComponent
except Exception:
    print("[ERROR] glyphsLib is required. Install with: pip install glyphsLib")
    sys.exit(1)


# Classification by glyph name suffixes
TOP_MARK_NAMES = {
    "acutecomb", "gravecomb", "circumflexcomb", "circumflexcomb.narrow",
    "caroncomb", "caroncomb.narrow", "caroncomb.alt",
    "brevecomb", "macroncomb", "tildecomb",
    "ringcomb", "dieresiscomb", "dieresiscomb.narrow",
    "hungarumlautcomb", "dotaccentcomb", "commaturnedabovecomb",
}
BOTTOM_MARK_NAMES = {
    "dotbelowcomb", "commaaccentcomb", "cedillacomb",
}
OVERLAY_MARK_NAMES = {"strokeshortcomb", "strokelongcomb"}
OGONEK_MARK_NAMES = {"ogonekcomb"}

# Some glyphs may be named by unicode like uni0306 etc.; provide partial mapping
UNICODE_TOP_PREFIXES = {"uni030", "uni034"}  # 0300..034F combining diacritics


def is_mark_glyph(g) -> bool:
    try:
        if getattr(g, "category", None) == "Mark":
            return True
    except Exception:
        pass
    # Fallback by name
    name = getattr(g, "name", "") or ""
    return name.endswith("comb") or any(name.startswith(p) for p in UNICODE_TOP_PREFIXES)


def mark_kind(gname: str) -> Optional[str]:
    if gname in TOP_MARK_NAMES or gname.startswith("uni030"):
        # Default to top for general 030x unless explicitly in other sets
        if gname in BOTTOM_MARK_NAMES:
            return "bottom"
        if gname in OVERLAY_MARK_NAMES:
            return "overlay"
        if gname in OGONEK_MARK_NAMES:
            return "ogonek"
        return "top"
    if gname in BOTTOM_MARK_NAMES:
        return "bottom"
    if gname in OVERLAY_MARK_NAMES:
        return "overlay"
    if gname in OGONEK_MARK_NAMES:
        return "ogonek"
    # For safety: infer by common substrings
    if any(k in gname for k in ("below", "cedilla", "commaaccent")):
        return "bottom"
    if any(k in gname for k in ("stroke",)):
        return "overlay"
    if "ogonek" in gname:
        return "ogonek"
    if gname.endswith("comb"):
        return "top"
    return None


def _axes_vec(m) -> Optional[Tuple]:
    v = getattr(m, "axes", None)
    if v is not None:
        try:
            return tuple(v)
        except Exception:
            pass
    w = getattr(m, "weightValue", None)
    if w is not None:
        try:
            return (float(w),)
        except Exception:
            pass
    return None


def find_master_layer(glyph, master_id: str):
    for l in getattr(glyph, "layers", []) or []:
        if getattr(l, "layerId", None) == master_id:
            return l
    for l in getattr(glyph, "layers", []) or []:
        if getattr(l, "associatedMasterId", None) == master_id:
            return l
    return None


def iter_path_points(layer) -> Iterable[Tuple[float, float]]:
    for sh in getattr(layer, "shapes", []) or []:
        # GSPath
        nodes = getattr(sh, "nodes", None)
        if nodes:
            for n in nodes:
                x = getattr(n, "x", None)
                y = getattr(n, "y", None)
                if x is None or y is None:
                    pos = getattr(n, "position", None)
                    if pos:
                        x, y = pos[0], pos[1]
                if x is not None and y is not None:
                    yield float(x), float(y)


def component_bbox(font: GSFont, layer, comp: GSComponent, master_id: str) -> Optional[Tuple[float, float, float, float]]:
    # Resolve referenced glyph
    ref_glyph = None
    try:
        cname = getattr(comp, "componentName", None) or getattr(comp, "name", None)
        if not cname:
            cname = getattr(comp, "ref", None)  # fallback
        if cname:
            ref_glyph = font.glyphs[cname]
    except Exception:
        pass
    if ref_glyph is None:
        return None
    ref_layer = find_master_layer(ref_glyph, master_id)
    if ref_layer is None:
        return None

    # Get bbox of referenced layer
    min_x = min_y = float("inf")
    max_x = max_y = float("-inf")
    for x, y in iter_path_points(ref_layer):
        if x < min_x: min_x = x
        if y < min_y: min_y = y
        if x > max_x: max_x = x
        if y > max_y: max_y = y
    if min_x == float("inf"):
        return None

    # Transform: support translation and scale
    sx = sy = 1.0
    tx = ty = 0.0
    # glyphsLib exposes .position and .scale on GSComponent in many versions
    try:
        pos = getattr(comp, "position", None)
        if pos:
            tx, ty = float(pos[0]), float(pos[1])
        else:
            tx = float(getattr(comp, "x", 0.0))
            ty = float(getattr(comp, "y", 0.0))
    except Exception:
        pass
    try:
        sc = getattr(comp, "scale", None)
        if sc:
            sx, sy = float(sc[0]), float(sc[1])
    except Exception:
        pass

    x0 = sx * min_x + tx
    y0 = sy * min_y + ty
    x1 = sx * max_x + tx
    y1 = sy * max_y + ty
    # Normalize if negative scale
    min_tx = min(x0, x1)
    max_tx = max(x0, x1)
    min_ty = min(y0, y1)
    max_ty = max(y0, y1)
    return (min_tx, min_ty, max_tx, max_ty)


def layer_bbox(font: GSFont, glyph, layer, master_id: str) -> Optional[Tuple[float, float, float, float]]:
    min_x = min_y = float("inf")
    max_x = max_y = float("-inf")

    # Paths
    has_points = False
    for x, y in iter_path_points(layer):
        has_points = True
        if x < min_x: min_x = x
        if y < min_y: min_y = y
        if x > max_x: max_x = x
        if y > max_y: max_y = y

    # Components
    for sh in getattr(layer, "shapes", []) or []:
        if isinstance(sh, GSComponent):
            bbox = component_bbox(font, layer, sh, master_id)
            if bbox:
                x0, y0, x1, y1 = bbox
                if x0 < min_x: min_x = x0
                if y0 < min_y: min_y = y0
                if x1 > max_x: max_x = x1
                if y1 > max_y: max_y = y1

    if min_x == float("inf"):
        # No outline; fallback to layer width centered baseline
        try:
            w = float(getattr(layer, "width", 0.0))
        except Exception:
            w = 0.0
        cx = w * 0.5
        return (cx, 0.0, cx, 0.0)

    return (min_x, min_y, max_x, max_y)


def get_anchor(layer, name: str) -> Optional[GSAnchor]:
    for a in getattr(layer, "anchors", []) or []:
        if getattr(a, "name", None) == name:
            return a
    return None


def set_anchor(layer, name: str, x: float, y: float) -> None:
    a = get_anchor(layer, name)
    if a is None:
        a = GSAnchor()
        a.name = name
        if getattr(layer, "anchors", None) is None:
            layer.anchors = []
        layer.anchors.append(a)
    # assign position robustly
    try:
        a.position = (float(x), float(y))
    except Exception:
        try:
            a.x = float(x); a.y = float(y)
        except Exception:
            pass


def filter_anchors(layer, allowed: Iterable[str]) -> int:
    allowed_set = set(allowed)
    anchors = getattr(layer, "anchors", None)
    if not anchors:
        return 0
    keep = [a for a in anchors if getattr(a, "name", None) in allowed_set]
    removed = len(anchors) - len(keep)
    if removed:
        layer.anchors = keep
    return removed


def normalize_file(path: Path) -> Dict[str, int]:
    font = GSFont(str(path))
    changed_glyphs = 0
    total_removed = 0
    total_set = 0

    # Build a quick map for master ids
    master_ids = [m.id for m in font.masters]

    for g in font.glyphs:
        if not is_mark_glyph(g):
            continue
        gname = getattr(g, "name", "") or ""
        kind = mark_kind(gname)
        if not kind:
            continue
        glyph_changed = False
        for mid in master_ids:
            layer = find_master_layer(g, mid)
            if layer is None:
                continue
            bbox = layer_bbox(font, g, layer, mid)
            if not bbox:
                continue
            x0, y0, x1, y1 = bbox
            cx = (x0 + x1) * 0.5
            cy = (y0 + y1) * 0.5

            if kind == "top":
                # Remove irrelevant anchors on this layer
                total_removed += filter_anchors(layer, ("_top", "top"))
                set_anchor(layer, "_top", cx, y0)
                set_anchor(layer, "top", cx, y1)
                total_set += 2
                glyph_changed = True
            elif kind == "bottom":
                total_removed += filter_anchors(layer, ("_bottom", "bottom"))
                set_anchor(layer, "_bottom", cx, y1)
                set_anchor(layer, "bottom", cx, y0)
                total_set += 2
                glyph_changed = True
            elif kind == "overlay":
                total_removed += filter_anchors(layer, ("_center", "center"))
                set_anchor(layer, "_center", cx, cy)
                set_anchor(layer, "center", cx, cy)
                total_set += 2
                glyph_changed = True
            elif kind == "ogonek":
                total_removed += filter_anchors(layer, ("_ogonek", "ogonek"))
                set_anchor(layer, "_ogonek", cx, y1)
                set_anchor(layer, "ogonek", cx, y0)
                total_set += 2
                glyph_changed = True
        if glyph_changed:
            changed_glyphs += 1

    if changed_glyphs:
        font.save(str(path))

    return {
        "glyphs_changed": changed_glyphs,
        "anchors_set": total_set,
        "anchors_removed": total_removed,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: normalize_mark_anchors.py sources/Akt.glyphs")
        return 2
    p = Path(argv[1])
    if not p.exists():
        print(f"[ERROR] File not found: {p}")
        return 2
    stats = normalize_file(p)
    print(
        "Normalization complete:\n"
        f"  Glyphs changed: {stats['glyphs_changed']}\n"
        f"  Anchors set/updated: {stats['anchors_set']}\n"
        f"  Irrelevant anchors removed: {stats['anchors_removed']}\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))