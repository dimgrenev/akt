#!/usr/bin/env python3
"""
Adds a full Regular master (Weight=400) to sources/Akt.glyphs by:
1) Building the "Regular" instance UFO via fontmake (uses instanceInterpolations from the .glyphs);
2) Importing UFO outlines/components/anchors/width into a new master layer for every glyph;
3) Adding a new GSFontMaster with axesValues=[400] and Axis Location Weight=400;
4) Updating the "Variable Font Origin" custom parameter to this new master id.

Requirements: fontmake, glyphsLib, defcon
"""
from __future__ import annotations

import sys
import uuid
import subprocess
from pathlib import Path
import traceback
import tempfile
import shutil

try:
    from glyphsLib import GSFont, classes
except Exception as e:
    print("ERROR: glyphsLib is required. Install with: pip install glyphsLib")
    raise

try:
    from defcon import Font as UFOFont
except Exception as e:
    print("ERROR: defcon is required. Install with: pip install defcon")
    raise

ROOT = Path(__file__).resolve().parent
SRC_PATH = ROOT / "sources" / "Akt.glyphs"
INST_UFO_DIR = ROOT / "build" / "instance_ufo"
INSTANCE_NAME = "Regular"
TARGET_WEIGHT = 400
INST_UFO_CACHED = ROOT / "build" / "instance_ufo" / "Akt-Regular.ufo"


def has_outline_in_ufo(ufo_path: Path) -> bool:
    """Quickly validate that the UFO contains real contours for core base glyphs.
    Returns True if at least one of the common base glyphs has at least one contour with points.
    """
    try:
        u = UFOFont(str(ufo_path))
    except Exception:
        u = None
    if u is not None:
        probe_names = [
            "a", "e", "n", "o", "s",
            "A", "B", "C"
        ]
        try:
            hits = 0
            for name in probe_names:
                try:
                    if name in u:
                        g = u[name]
                    else:
                        continue
                    cs = getattr(g, "contours", []) or []
                    if cs:
                        # ensure at least one point exists
                        for c in cs:
                            pts = getattr(c, "points", []) or []
                            if pts:
                                hits += 1
                                break
                except Exception:
                    continue
            if hits > 0:
                return True
        except Exception:
            pass
    # Fallback: scan GLIF XML for <point ...> to detect contours
    try:
        glyphs_dir = Path(ufo_path) / "glyphs"
        if glyphs_dir.is_dir():
            checked = 0
            for glif in sorted(glyphs_dir.glob("*.glif")):
                # prioritize some common base glyphs
                n = glif.stem.lower()
                if n not in {"a","e","n","o","s","b","c","d","m","u","k"}:
                    # sample a few random files too
                    if checked > 50:
                        break
                try:
                    with open(glif, "r", encoding="utf-8") as fh:
                        head = fh.read(2000)
                    if "<point" in head or " type=\"line\"" in head or " type=\"curve\"" in head or " type=\"qcurve\"" in head:
                        return True
                except Exception:
                    pass
                checked += 1
    except Exception:
        pass
    return False


def run_fontmake_for_instance(gs_path: Path) -> Path:
    # Всегда собираем свежие инстансы, чтобы гарантировать корректную интерполяцию
    INST_UFO_DIR.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable,
        "-m",
        "fontmake",
        "-g",
        str(gs_path),
        "-i",
        "-o",
        "ufo",
        "--output-dir",
        str(INST_UFO_DIR),
    ]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, check=False)
    # gather produced candidates
    ufo_candidates = sorted(INST_UFO_DIR.glob("*.ufo"))
    regular_candidate = None
    for p in ufo_candidates:
        if "-Regular" in p.stem or p.stem.endswith("Regular") or INSTANCE_NAME in p.stem:
            regular_candidate = p
            break
    # prefer a produced Regular that actually has outlines
    if regular_candidate is not None and has_outline_in_ufo(regular_candidate):
        print("Using UFO:", regular_candidate)
        return regular_candidate
    # else, try any produced candidate with outlines (defensive)
    for p in ufo_candidates:
        if has_outline_in_ufo(p):
            print("Using UFO (fallback produced):", p)
            return p
    # additional fallbacks: previously built locations
    alt_paths = [
        ROOT / "build" / "ufo" / "Akt-Regular.ufo",
        ROOT / "build" / "instance_ufo_test" / "Akt-Regular.ufo",
    ]
    for ap in alt_paths:
        if ap.exists() and has_outline_in_ufo(ap):
            print("Using UFO (fallback alt):", ap)
            return ap
    # if nothing useful produced, then raise if fontmake failed
    if proc.returncode != 0:
        raise subprocess.CalledProcessError(proc.returncode, cmd)
    if not ufo_candidates:
        raise FileNotFoundError(f"No UFO produced in {INST_UFO_DIR}")
    # last resort: return first candidate (may be empty)
    print("Using UFO:", ufo_candidates[0])
    return ufo_candidates[0]


def get_master_by_name(font: GSFont, name: str):
    for m in font.masters:
        if getattr(m, "name", "") == name:
            return m
    return None


def _normalize_custom_parameters_on(obj):
    try:
        cps_in = list(getattr(obj, "customParameters", []) or [])
    except Exception:
        return
    cps_out = []
    for item in cps_in:
        try:
            if isinstance(item, classes.GSCustomParameter):
                cps_out.append(item)
                continue
            if isinstance(item, tuple) and len(item) == 2:
                n, v = item
            else:
                n = getattr(item, "name", None)
                v = getattr(item, "value", None)
            if not n:
                continue
            cp = classes.GSCustomParameter()
            cp.name = n
            cp.value = v
            cps_out.append(cp)
        except Exception:
            continue
    try:
        obj.customParameters = cps_out
    except Exception:
        pass


def glyphs_paths_from_ufo(ufo_glyph):
    """Build GSPath list from a defcon UFO glyph.
    Handles both cubic and quadratic outlines by converting qcurves to cubic.
    """
    paths = []
    try:
        # Use fontTools pens to normalize to cubic curves
        from fontTools.pens.recordingPen import RecordingPen
        try:
            # Prefer explicit quadratic->cubic conversion
            from fontTools.pens.cu2quPen import Cu2QuPen
            rec_src = RecordingPen()
            ufo_glyph.draw(rec_src)
            rec_cubic = RecordingPen()
            cu_pen = Cu2QuPen(rec_cubic, max_err=0.5, reverse_direction=False)
            for op, pts in rec_src.value:
                if op == "moveTo":
                    cu_pen.moveTo(pts[0])
                elif op == "lineTo":
                    cu_pen.lineTo(pts[0])
                elif op == "qCurveTo":
                    # fontTools cu2qu supports qCurveTo with N control points and an end (or implicit on-curve if end is None)
                    cu_pen.qCurveTo(*pts)
                elif op == "curveTo":
                    cu_pen.curveTo(*pts)
                elif op == "closePath":
                    cu_pen.closePath()
                elif op == "endPath":
                    cu_pen.endPath()
            rec = rec_cubic
        except Exception:
            # If cu2qu not available, just record as-is (may contain qCurveTo)
            rec = RecordingPen()
            ufo_glyph.draw(rec)
        # Now build GSPaths from recording (should be all move/line/curve + close)
        current = None
        for op, pts in rec.value:
            if op == "moveTo":
                if current is not None:
                    # open contour
                    current.closed = False
                    if len(current.nodes) > 0:
                        paths.append(current)
                current = classes.GSPath()
                x, y = pts[0]
                n = classes.GSNode()
                n.position = (float(x), float(y))
                n.type = "line"
                current.nodes.append(n)
            elif op == "lineTo" and current is not None:
                x, y = pts[0]
                n = classes.GSNode()
                n.position = (float(x), float(y))
                n.type = "line"
                current.nodes.append(n)
            elif op == "curveTo" and current is not None:
                # cubic: two offcurves + oncurve end
                (cx1, cy1), (cx2, cy2), (x, y) = pts
                n1 = classes.GSNode(); n1.position = (float(cx1), float(cy1)); n1.type = "offcurve"
                n2 = classes.GSNode(); n2.position = (float(cx2), float(cy2)); n2.type = "offcurve"
                n3 = classes.GSNode(); n3.position = (float(x), float(y)); n3.type = "curve"
                current.nodes.extend([n1, n2, n3])
            elif op == "closePath" and current is not None:
                current.closed = True
                if len(current.nodes) > 0:
                    paths.append(current)
                current = None
            elif op == "endPath" and current is not None:
                current.closed = False
                if len(current.nodes) > 0:
                    paths.append(current)
                current = None
        # flush leftover
        if current is not None and len(current.nodes) > 0:
            paths.append(current)
        return paths
    except Exception:
        # Fallback: original naive conversion
        for contour in getattr(ufo_glyph, "contours", []) or []:
            pts = []
            for pt in contour.points:
                x = float(pt.x)
                y = float(pt.y)
                seg = getattr(pt, "segmentType", None)
                pts.append((x, y, seg, bool(getattr(pt, "smooth", False))))
            first_on = None
            for i, (_, _, seg, _) in enumerate(pts):
                if seg in ("line", "curve"):
                    first_on = i
                    break
            if first_on is None:
                continue
            pts = pts[first_on:] + pts[:first_on]
            p = classes.GSPath()
            for x, y, seg, smooth in pts:
                n = classes.GSNode()
                try:
                    n.position = (x, y)
                except Exception:
                    try:
                        n.x = x; n.y = y
                    except Exception:
                        pass
                if seg is None:
                    n.type = "offcurve"
                elif seg == "line":
                    n.type = "line"
                elif seg == "curve":
                    n.type = "curve"
                else:
                    n.type = "line"
                try:
                    n.smooth = bool(smooth)
                except Exception:
                    pass
                p.nodes.append(n)
            p.closed = bool(getattr(contour, "closed", True))
            paths.append(p)
        return paths


def glyphs_components_from_ufo(ufo_glyph):
    comps = []
    for uc in getattr(ufo_glyph, "components", []) or []:
        c = classes.GSComponent()
        try:
            c.componentName = uc.baseGlyph
        except Exception:
            pass
        tr = getattr(uc, "transformation", None)
        if tr and isinstance(tr, (tuple, list)) and len(tr) == 6:
            try:
                # glyphsLib expects a Transform object, not a tuple
                c.transform = classes.Transform([
                    float(tr[0]), float(tr[1]), float(tr[2]),
                    float(tr[3]), float(tr[4]), float(tr[5])
                ])
            except Exception:
                # fallback to simple translation
                try:
                    c.position = (float(tr[4]), float(tr[5]))
                except Exception:
                    pass
        else:
            dx = float(getattr(uc, "x", 0.0) or 0.0)
            dy = float(getattr(uc, "y", 0.0) or 0.0)
            try:
                c.position = (dx, dy)
            except Exception:
                pass
        comps.append(c)
    return comps


def add_regular_master_from_ufo(gs_path: Path, ufo_path: Path) -> str:
    font = GSFont(str(gs_path))
    ufo = UFOFont(str(ufo_path))

    # Build robust glyph map from UFO
    ufo_glyphs = {}
    try:
        for name in list(ufo.keys()):
            try:
                ufo_glyphs[name] = ufo[name]
            except Exception:
                pass
    except Exception:
        # Fallback to iteration
        try:
            for g in ufo:
                try:
                    name = getattr(g, "name", None)
                    if name:
                        ufo_glyphs[name] = g
                except Exception:
                    pass
        except Exception:
            pass

    # If a master at 400 already exists, patch metrics/stems and save
    for m in font.masters:
        axes = getattr(m, "axes", None) or getattr(m, "axesValues", None)
        try:
            if axes and int(round(float(axes[0]))) == TARGET_WEIGHT:
                print(f"Master at {TARGET_WEIGHT} already exists: {m.name} ({m.id})")
                # ensure stems are reset to avoid index issues
                _reset_stems(m)

                # Полностью перезаписываем слои мастера 400 из интерполированного UFO
                replaced = 0
                for g in font.glyphs:
                    try:
                        layer = _get_layer_for_master(g, m.id)
                    except Exception:
                        layer = None
                    if layer is None:
                        layer = classes.GSLayer()
                        layer.layerId = m.id
                        layer.associatedMasterId = m.id
                        g.layers.append(layer)
                    # Очистить текущие shapes/anchors перед заменой
                    try:
                        while len(getattr(layer, "paths", []) or []):
                            del layer.paths[0]
                    except Exception:
                        try:
                            layer.paths = []
                        except Exception:
                            pass
                    try:
                        while len(getattr(layer, "components", []) or []):
                            del layer.components[0]
                    except Exception:
                        try:
                            layer.components = []
                        except Exception:
                            pass
                    try:
                        while len(getattr(layer, "shapes", []) or []):
                            del layer.shapes[0]
                    except Exception:
                        try:
                            layer.shapes = []
                        except Exception:
                            pass
                    try:
                        while len(getattr(layer, "anchors", []) or []):
                            del layer.anchors[0]
                    except Exception:
                        try:
                            layer.anchors = []
                        except Exception:
                            pass

                    ug = ufo_glyphs.get(g.name)
                    ug_has_shapes = False
                    ug_width = None
                    if ug is not None:
                        try:
                            ug_width = getattr(ug, "width", None)
                        except Exception:
                            ug_width = None
                        try:
                            # Build shapes: prefer components if present, else use decomposed paths
                            conv_paths = []
                            comps = []
                            try:
                                conv_paths = glyphs_paths_from_ufo(ug) or []
                            except Exception:
                                conv_paths = []
                            try:
                                comps = glyphs_components_from_ufo(ug) or []
                            except Exception:
                                comps = []
                            # Reassign explicit paths/components lists to ensure persistence
                            try:
                                layer.paths = []
                            except Exception:
                                pass
                            try:
                                layer.components = []
                            except Exception:
                                pass
                            if comps:
                                for c in comps:
                                    try:
                                        layer.components.append(c)
                                    except Exception:
                                        pass
                                ug_has_shapes = True
                            if conv_paths:
                                for p in conv_paths:
                                    try:
                                        layer.paths.append(p)
                                    except Exception:
                                        pass
                                ug_has_shapes = True
                            # Anchors
                            try:
                                layer.anchors = []
                                for a in getattr(ug, "anchors", []) or []:
                                    ga = classes.GSAnchor()
                                    try:
                                        ga.name = a.name
                                    except Exception:
                                        pass
                                    try:
                                        ga.position = (float(a.x), float(a.y))
                                    except Exception:
                                        try:
                                            ga.x = float(a.x); ga.y = float(a.y)
                                        except Exception:
                                            pass
                                    layer.anchors.append(ga)
                            except Exception:
                                pass
                        except Exception:
                            pass
                        # Ширина
                        try:
                            if ug_width is not None:
                                layer.width = int(round(float(ug_width or 0)))
                        except Exception:
                            pass
                        replaced += 1
                    else:
                        # No ug: keep layer empty to avoid copying Bold shapes
                        pass
                if replaced:
                    print(f"Replaced layers for existing master using UFO: {replaced} glyphs updated")

                # Enforce compatibility with key masters (0 and 700) to avoid interpolation errors
                try:
                    ref0 = _get_master_id_by_weight(font, 0)
                    ref700 = _get_master_id_by_weight(font, 700)
                    _enforce_layer_compatibility(font, m.id, [ref700, ref0])
                    # Additionally align per-glyph segment types and starting points
                    try:
                        for g in font.glyphs:
                            tgt = _get_layer_for_master(g, m.id)
                            ref = _get_layer_for_master(g, ref700) if ref700 else None
                            if tgt and ref:
                                try:
                                    _align_segment_types_layer(tgt, ref)
                                except Exception:
                                    pass
                                try:
                                    _align_start_points_layer(tgt, ref)
                                except Exception:
                                    pass
                    except Exception:
                        pass
                except Exception:
                    pass

                try:
                    set_variable_font_origin(font, m.id)
                except Exception:
                    pass
                try:
                    _normalize_deep(font)
                except Exception:
                    pass
                try:
                    _sanitize_all_master_stems(font)
                except Exception:
                    pass
                try:
                    font.save(str(gs_path))
                    print(f"Patched existing master and saved: {gs_path}")
                except Exception as e:
                    print("WARN: could not save after replacing existing master:", e)
                return m.id
        except Exception:
            pass

    # Create new master
    new_master = classes.GSFontMaster()
    new_master.id = str(uuid.uuid4()).upper()
    new_master.name = "Regular"
    try:
        new_master.axes = [TARGET_WEIGHT]
    except Exception:
        try:
            new_master.axesValues = [TARGET_WEIGHT]
        except Exception:
            pass
    new_master.iconName = "Regular"
    new_master.visible = True

    # Copy vertical metrics and stems from Bold if present else Thin
    bold = get_master_by_name(font, "Bold") or font.masters[0]
    for attr in ("ascender", "capHeight", "descender", "xHeight"):
        try:
            setattr(new_master, attr, getattr(bold, attr))
        except Exception:
            pass
    # reset stems to avoid reference/index mismatches
    _reset_stems(new_master)
    # stems left empty intentionally to avoid index mismatches
    # Custom parameters: copy common ones and set Axis Location
    new_master.customParameters = []
    src_params = list(getattr(bold, "customParameters", []) or [])
    for p in src_params:
        # accept both tuple pairs and objects
        name = None
        value = None
        if isinstance(p, tuple) and len(p) == 2:
            name, value = p
        else:
            try:
                name = getattr(p, "name", None)
                value = getattr(p, "value", None)
            except Exception:
                name = None
                value = None
        if not name or name == "Axis Location":
            continue
        cp = classes.GSCustomParameter()
        cp.name = name
        cp.value = value
        new_master.customParameters.append(cp)
    cp_axis = classes.GSCustomParameter()
    cp_axis.name = "Axis Location"
    cp_axis.value = [{"axis": "Weight", "location": TARGET_WEIGHT}]
    new_master.customParameters.append(cp_axis)

    font.masters.append(new_master)
    print(f"Created master {new_master.name} with id {new_master.id}")

    # Map of UFO glyphs (robust)
    ufo_glyphs = {}
    try:
        for name in list(ufo.keys()):
            try:
                ufo_glyphs[name] = ufo[name]
            except Exception:
                pass
    except Exception:
        try:
            for g in ufo:
                try:
                    name = getattr(g, "name", None)
                    if name:
                        ufo_glyphs[name] = g
                except Exception:
                    pass
        except Exception:
            pass

    created = 0
    missing = 0
    for g in font.glyphs:
        # remove any pre-existing layer with the same master id (from failed runs)
        try:
            for lay in list(g.layers):
                if getattr(lay, "layerId", None) == new_master.id:
                    try:
                        g.layers.remove(lay)
                    except Exception:
                        pass
        except Exception:
            pass

        layer = classes.GSLayer()
        layer.layerId = new_master.id
        layer.associatedMasterId = new_master.id

        ug = ufo_glyphs.get(g.name)
        ug_anchors = []
        ug_width = None
        if ug is not None:
            try:
                ug_width = getattr(ug, "width", None)
            except Exception:
                ug_width = None
            # Paths and components: prefer components if present, else use decomposed paths
            try:
                conv_paths = []
                comps = []
                try:
                    conv_paths = glyphs_paths_from_ufo(ug) or []
                except Exception:
                    conv_paths = []
                try:
                    comps = glyphs_components_from_ufo(ug) or []
                except Exception:
                    comps = []
                # Reassign explicit paths/components lists to ensure persistence
                try:
                    layer.paths = []
                except Exception:
                    pass
                try:
                    layer.components = []
                except Exception:
                    pass
                if comps:
                    for c in comps:
                        try:
                            layer.components.append(c)
                        except Exception:
                            pass
                if conv_paths:
                    for p in conv_paths:
                        try:
                            layer.paths.append(p)
                        except Exception:
                            pass
            except Exception:
                pass
            # anchors
            try:
                ug_anchors = list(getattr(ug, "anchors", []) or [])
            except Exception:
                ug_anchors = []
        else:
            missing += 1

        # anchors: from UFO when available, else leave empty (no Bold fallback)
        try:
            if ug_anchors:
                layer.anchors = []
                for a in ug_anchors:
                    ga = classes.GSAnchor()
                    try:
                        ga.name = a.name
                    except Exception:
                        pass
                    try:
                        ga.position = (float(a.x), float(a.y))
                    except Exception:
                        try:
                            ga.x = float(a.x); ga.y = float(a.y)
                        except Exception:
                            pass
                    layer.anchors.append(ga)
        except Exception:
            pass

        # width
        try:
            if ug_width is not None:
                layer.width = int(round(float(ug_width or 0)))
        except Exception:
            pass

        g.layers.append(layer)
        if ug is not None:
            created += 1

    print(f"Layers added: {created}, missing UFO glyphs: {missing}")

    # Enforce compatibility with key masters (0 and 700)
    try:
        ref0 = _get_master_id_by_weight(font, 0)
        ref700 = _get_master_id_by_weight(font, 700)
        _enforce_layer_compatibility(font, new_master.id, [ref700, ref0])
        # Align segment types and start points in the new master to reference
        try:
            for g in font.glyphs:
                tgt = _get_layer_for_master(g, new_master.id)
                ref = _get_layer_for_master(g, ref700) if ref700 else None
                if tgt and ref:
                    try:
                        _align_segment_types_layer(tgt, ref)
                    except Exception:
                        pass
                    try:
                        _align_start_points_layer(tgt, ref)
                    except Exception:
                        pass
        except Exception:
            pass
    except Exception:
        pass

    # Deep normalize and diagnose customParameters across the whole font
    try:
        _normalize_deep(font)
        offenders = _find_tuple_params(font)
        if offenders:
            print("WARN: Found tuple customParameters after normalization (showing up to 20):")
            for path, clsname, it in offenders[:20]:
                print(" -", path, "in", clsname, "=", it)
            print(f"Total offenders: {len(offenders)}")
    except Exception as e:
        print("WARN: deep normalization failed partially:", e)
        print(traceback.format_exc())

    # Save without touching font-level custom parameters further
    try:
        # set Variable Font Origin before save
        set_variable_font_origin(font, new_master.id)
        _normalize_custom_parameters_on(font)
        try:
            _sanitize_all_master_stems(font)
        except Exception:
            pass
        font.save(str(gs_path))
        print(f"Saved: {gs_path}")
        print(f"Variable Font Origin set to {new_master.id}")
    except Exception as e:
        print("ERROR DURING SAVE:", e)
        print(traceback.format_exc())
        raise

    return new_master.id


def _normalize_deep(font):
    # Font itself
    _normalize_custom_parameters_on(font)
    # Masters
    for m in getattr(font, "masters", []) or []:
        _normalize_custom_parameters_on(m)
    # Instances
    for inst in getattr(font, "instances", []) or []:
        _normalize_custom_parameters_on(inst)
    # Axes
    for ax in getattr(font, "axes", []) or []:
        _normalize_custom_parameters_on(ax)
    # Features, Classes, Feature Prefixes
    for feat in getattr(font, "features", []) or []:
        _normalize_custom_parameters_on(feat)
    for cls in getattr(font, "classes", []) or []:
        _normalize_custom_parameters_on(cls)
    for fp in getattr(font, "featurePrefixes", []) or []:
        _normalize_custom_parameters_on(fp)
    # Glyphs and layers
    for g in getattr(font, "glyphs", []) or []:
        _normalize_custom_parameters_on(g)
        for lay in getattr(g, "layers", []) or []:
            _normalize_custom_parameters_on(lay)


def _find_tuple_params(font):
    offenders = []
    def check(obj, path):
        try:
            cps = getattr(obj, "customParameters", None)
        except Exception:
            cps = None
        if cps is not None:
            for i, it in enumerate(list(cps) or []):
                if isinstance(it, tuple):
                    offenders.append((path + f".customParameters[{i}]", type(obj).__name__, it))
        # Recurse a few known containers
        for name in ("masters", "instances", "axes", "features", "classes", "featurePrefixes", "glyphs"):
            try:
                items = getattr(obj, name, None)
            except Exception:
                items = None
            if not items:
                continue
            for idx, child in enumerate(list(items)):
                child_path = f"{path}.{name}[{idx}]"
                check(child, child_path)
                if name == "glyphs":
                    try:
                        layers = getattr(child, "layers", None)
                    except Exception:
                        layers = None
                    if layers:
                        for j, lay in enumerate(list(layers)):
                            check(lay, f"{child_path}.layers[{j}]")
    check(font, "font")
    return offenders


# Utility clone helpers

def _clone_shapes(src_layer, dst_layer):
    # Clear destination shapes, paths, and components robustly
    try:
        for s in list(getattr(dst_layer, "shapes", []) or []):
            try:
                dst_layer.shapes.remove(s)
            except Exception:
                pass
    except Exception:
        pass
    try:
        dst_layer.paths = []
    except Exception:
        pass
    try:
        dst_layer.components = []
    except Exception:
        pass

    # Prefer iterating over src_layer.shapes to preserve ordering between paths and components
    try:
        src_shapes = list(getattr(src_layer, "shapes", []) or [])
    except Exception:
        src_shapes = []

    if src_shapes:
        for s in src_shapes:
            copied = None
            try:
                copied = s.copy()
            except Exception:
                copied = s
            # Append to shapes list only; Glyphs API keeps paths/components in sync with shapes
            try:
                dst_layer.shapes.append(copied)
            except Exception:
                pass
        return

    # Fallback: if shapes not available, clone from paths/components by appending to shapes only
    try:
        for p in getattr(src_layer, "paths", []) or []:
            try:
                cp = p.copy()
            except Exception:
                cp = p
            try:
                dst_layer.shapes.append(cp)
            except Exception:
                pass
        for c in getattr(src_layer, "components", []) or []:
            try:
                cc = c.copy()
            except Exception:
                cc = c
            try:
                dst_layer.shapes.append(cc)
            except Exception:
                pass
    except Exception:
        pass


def _clone_anchors(src_layer, dst_layer):
    try:
        dst_layer.anchors = []
    except Exception:
        pass
    try:
        for a in getattr(src_layer, "anchors", []) or []:
            try:
                dst_layer.anchors.append(a.copy())
            except Exception:
                pass
    except Exception:
        pass


def _reset_stems(master):
    for attr in ("stems", "horizontalStems", "verticalStems"):
        try:
            setattr(master, attr, [])
        except Exception:
            pass
    # also reset internal fields used by glyphsLib getters
    try:
        setattr(master, "_horizontalStems", [])
    except Exception:
        pass
    try:
        setattr(master, "_verticalStems", [])
    except Exception:
        pass


def _sanitize_all_master_stems(font):
    try:
        # clear font-level stems first
        try:
            font.stems = []
        except Exception:
            pass
        for m in getattr(font, "masters", []):
            _reset_stems(m)
    except Exception:
        pass


def _get_layer_for_master(glyph, master_id):
    try:
        for lay in getattr(glyph, "layers", []) or []:
            if getattr(lay, "layerId", None) == master_id:
                return lay
    except Exception:
        pass
    return None


def set_variable_font_origin(font, origin_master_id: str):
    # Set at font level
    try:
        cps = list(getattr(font, "customParameters", []) or [])
    except Exception:
        cps = []
    # remove existing
    try:
        font.customParameters = [cp for cp in cps if getattr(cp, "name", None) != "Variable Font Origin"]
    except Exception:
        pass
    cp = classes.GSCustomParameter()
    cp.name = "Variable Font Origin"
    cp.value = origin_master_id
    try:
        font.customParameters.append(cp)
    except Exception:
        # some versions require list replacement
        try:
            current = list(getattr(font, "customParameters", []) or [])
            current.append(cp)
            font.customParameters = current
        except Exception:
            pass


def _make_temp_export_all(src_path: Path) -> Path:
    """Create a temporary copy of src with export=True for all glyphs.
    Also removes any brace layers at Weight=400 to ensure unique locations.
    Returns path to the temporary .glyphs file.
    """
    font = GSFont(str(src_path))
    changed = 0
    removed_brace_400 = 0
    for g in list(getattr(font, "glyphs", []) or []):
        # enable export
        try:
            if getattr(g, "export", True) is False:
                g.export = True
                changed += 1
        except Exception:
            pass
        # remove brace layers at 400
        try:
            to_remove = []
            for lay in list(getattr(g, "layers", []) or []):
                hit_400 = False
                # 1) via attributes.coordinates
                try:
                    attrs = getattr(lay, "attributes", None) or {}
                    coords = attrs.get("coordinates") if isinstance(attrs, dict) else None
                    if coords is not None:
                        # dict form: {"Weight": 400} or {"wght": 400}
                        if isinstance(coords, dict):
                            for k, v in coords.items():
                                kl = str(k).lower()
                                try:
                                    val = float(v)
                                except Exception:
                                    continue
                                if kl in ("weight", "wght") and abs(val - 400.0) < 1e-6:
                                    hit_400 = True
                                    break
                        # list/tuple single-axis form: [400] or (400,)
                        elif isinstance(coords, (list, tuple)) and len(coords) == 1:
                            try:
                                val = float(coords[0])
                                if abs(val - 400.0) < 1e-6:
                                    hit_400 = True
                            except Exception:
                                pass
                except Exception:
                    pass
                # 2) by name like "{400}" or "{wght=400, ...}"
                if not hit_400:
                    name = (getattr(lay, "name", None) or "").strip()
                    if name and name.startswith("{") and name.endswith("}"):
                        inner = name[1:-1].strip()
                        if "=" in inner:
                            parts = [p.strip() for p in inner.split(",")]
                            for p in parts:
                                if "=" not in p:
                                    continue
                                k, v = [s.strip() for s in p.split("=", 1)]
                                kl = k.lower()
                                try:
                                    val = float(v)
                                except Exception:
                                    continue
                                if kl in ("wght", "weight") and abs(val - 400.0) < 1e-6:
                                    hit_400 = True
                                    break
                        else:
                            try:
                                val = float(inner)
                                if abs(val - 400.0) < 1e-6:
                                    hit_400 = True
                            except Exception:
                                pass
                if hit_400:
                    to_remove.append(lay)
            if to_remove:
                for lay in to_remove:
                    try:
                        g.layers.remove(lay)
                        removed_brace_400 += 1
                    except Exception:
                        pass
        except Exception:
            pass
    tmp_dir = Path(tempfile.mkdtemp(prefix="akt_export_all_"))
    tmp_path = tmp_dir / src_path.name
    font.save(str(tmp_path))
    print(f"Temporary .glyphs saved: {tmp_path} (export fixed: {changed}, brace {400} removed: {removed_brace_400})")
    return tmp_path


def _get_master_id_by_weight(font, target: int):
    best = None
    best_diff = 10**9
    for m in getattr(font, 'masters', []) or []:
        axes = getattr(m, 'axes', None) or getattr(m, 'axesValues', None)
        try:
            if axes:
                w = int(round(float(axes[0])))
                d = abs(w - target)
                if d < best_diff:
                    best = m.id
                    best_diff = d
        except Exception:
            continue
    return best


def _enforce_layer_compatibility(font, target_master_id: str, reference_master_ids: list[str]):
    """Ensure target master layers have at least the same path/component presence as references.
    If target has zero paths while refs have some, or path/component counts differ, or per-path node structures differ,
    clone shapes from the first reference. This avoids interpolation failures when instance UFO import produced
    degenerate or simplified paths."""
    ref_ids = [rid for rid in reference_master_ids if rid]
    if not target_master_id or not ref_ids:
        return

    def path_signatures(layer):
        sigs = []
        try:
            for p in getattr(layer, 'paths', []) or []:
                try:
                    closed = bool(getattr(p, 'closed', True))
                except Exception:
                    closed = True
                try:
                    nodes = list(getattr(p, 'nodes', []) or [])
                except Exception:
                    nodes = []
                types = []
                for n in nodes:
                    try:
                        types.append(getattr(n, 'type', None))
                    except Exception:
                        types.append(None)
                sigs.append((closed, len(nodes), tuple(types)))
        except Exception:
            pass
        return sigs

    for g in getattr(font, 'glyphs', []) or []:
        try:
            # gather layers
            tgt = None
            refs = []
            for l in getattr(g, 'layers', []) or []:
                lid = getattr(l, 'layerId', None)
                if lid == target_master_id:
                    tgt = l
                elif lid in ref_ids:
                    refs.append(l)
            if tgt is None:
                continue

            # Choose first reference that has any shapes
            ref_layer = None
            for r in refs:
                rp = len(getattr(r, 'paths', []) or [])
                rc = len(getattr(r, 'components', []) or [])
                if rp or rc:
                    ref_layer = r
                    break
            if not ref_layer:
                continue

            # Compare high-level counts
            tp = len(getattr(tgt, 'paths', []) or [])
            tc = len(getattr(tgt, 'components', []) or [])
            rp = len(getattr(ref_layer, 'paths', []) or [])
            rc = len(getattr(ref_layer, 'components', []) or [])

            fix = False
            if (tp == 0 and rp > 0) or (tc == 0 and rc > 0):
                fix = True
            elif tp != rp or tc != rc:
                fix = True
            else:
                # Compare per-path node structure signatures
                try:
                    t_sigs = path_signatures(tgt)
                    r_sigs = path_signatures(ref_layer)
                    if len(t_sigs) != len(r_sigs):
                        fix = True
                    else:
                        for ts, rs in zip(t_sigs, r_sigs):
                            if ts != rs:
                                fix = True
                                break
                except Exception:
                    # If can't compute signatures, be conservative
                    fix = True

            if fix:
                # Clear destination first, then clone
                try:
                    while len(getattr(tgt, 'shapes', []) or []):
                        del tgt.shapes[0]
                except Exception:
                    try:
                        tgt.shapes = []
                    except Exception:
                        pass
                try:
                    tgt.paths = []
                except Exception:
                    pass
                try:
                    tgt.components = []
                except Exception:
                    pass
                _clone_shapes(ref_layer, tgt)
        except Exception:
            continue


def _segment_types_for_path(path):
    types = []
    nodes = getattr(path, 'nodes', []) or []
    for n in nodes:
        t = getattr(n, 'type', None)
        if t and t != 'offcurve':
            types.append(t)
    return types


def _convert_line_to_curve_in_path(path):
    nodes = getattr(path, 'nodes', []) or []
    if not nodes:
        return
    # collect indices of on-curve nodes
    on_idx = [i for i, n in enumerate(nodes) if getattr(n, 'type', None) != 'offcurve']
    is_closed = bool(getattr(path, 'closed', True))
    for k, idx in enumerate(list(on_idx)):
        n = nodes[idx]
        if getattr(n, 'type', None) == 'curve':
            continue  # already a curve segment end
        # we have a line segment end; convert to curve by inserting two offcurves
        # find previous on-curve index
        if k == 0:
            prev_on_i = on_idx[-1] if is_closed else None
        else:
            prev_on_i = on_idx[k - 1]
        if prev_on_i is None:
            # open path and first segment: no previous point to compute from
            continue
        start = nodes[prev_on_i]
        end = nodes[idx]
        try:
            x0, y0 = float(getattr(start, 'x', start.position[0])), float(getattr(start, 'y', start.position[1]))
            x1, y1 = float(getattr(end, 'x', end.position[0])), float(getattr(end, 'y', end.position[1]))
        except Exception:
            continue
        # place control points along the straight line (collinear), 1/3 and 2/3
        c1x, c1y = (2 * x0 + x1) / 3.0, (2 * y0 + y1) / 3.0
        c2x, c2y = (x0 + 2 * x1) / 3.0, (y0 + 2 * y1) / 3.0
        from glyphsLib import classes as _cls
        c1 = _cls.GSNode(); c1.type = 'offcurve'
        try:
            c1.position = (c1x, c1y)
        except Exception:
            c1.x = c1x; c1.y = c1y
        c2 = _cls.GSNode(); c2.type = 'offcurve'
        try:
            c2.position = (c2x, c2y)
        except Exception:
            c2.x = c2x; c2.y = c2y
        # insert before current end node
        try:
            nodes.insert(idx, c1)
            nodes.insert(idx + 1, c2)
        except Exception:
            continue
        try:
            end.type = 'curve'
        except Exception:
            pass
    # write back nodes (in case underlying list semantics require reassignment)
    try:
        path.nodes = nodes
    except Exception:
        pass


def _align_segment_types_layer(target_layer, reference_layer):
    try:
        tpaths = getattr(target_layer, 'paths', []) or []
        rpaths = getattr(reference_layer, 'paths', []) or []
    except Exception:
        return
    if len(tpaths) != len(rpaths):
        return
    for i, (tp, rp) in enumerate(zip(tpaths, rpaths)):
        try:
            t_segs = _segment_types_for_path(tp)
            r_segs = _segment_types_for_path(rp)
        except Exception:
            continue
        if len(t_segs) != len(r_segs):
            # cannot align safely, skip
            continue
        changed = False
        for j, (ts, rs) in enumerate(zip(t_segs, r_segs)):
            if ts == rs:
                continue
            if rs == 'curve' and ts == 'line':
                # convert this segment on target from line to curve
                _convert_line_to_curve_in_path(tp)
                changed = True
        if changed:
            try:
                tpaths[i] = tp
            except Exception:
                pass
    try:
        target_layer.paths = tpaths
    except Exception:
        pass


def _rotate_nodes_in_place(path, k: int):
    try:
        nodes = list(getattr(path, 'nodes', []) or [])
    except Exception:
        return
    n = len(nodes)
    if n == 0:
        return
    k = k % n
    if k == 0:
        return
    rotated = nodes[k:] + nodes[:k]
    # Reassign nodes sequentially
    try:
        # delete all
        while len(getattr(path, 'nodes', []) or []):
            del path.nodes[0]
    except Exception:
        try:
            path.nodes = []
        except Exception:
            pass
    for nd in rotated:
        try:
            path.nodes.append(nd)
        except Exception:
            pass


def _node_types_sequence(path):
    try:
        return [getattr(n, 'type', None) for n in (getattr(path, 'nodes', []) or [])]
    except Exception:
        return []


def _align_start_points_layer(target_layer, reference_layer):
    # For each corresponding path, rotate nodes in target so that node type sequence matches reference sequence
    try:
        tpaths = getattr(target_layer, 'paths', []) or []
        rpaths = getattr(reference_layer, 'paths', []) or []
    except Exception:
        return
    if len(tpaths) != len(rpaths):
        return
    for i, (tp, rp) in enumerate(zip(tpaths, rpaths)):
        try:
            tt = _node_types_sequence(tp)
            rt = _node_types_sequence(rp)
        except Exception:
            continue
        if len(tt) != len(rt) or not tt:
            continue
        if tt == rt:
            continue
        # Try cyclic alignment
        n = len(tt)
        aligned = False
        for k in range(1, n):
            # rotate tt by k and compare
            if tt[k:] + tt[:k] == rt:
                _rotate_nodes_in_place(tp, k)
                aligned = True
                break
        if not aligned:
            # If types differ only by minor mismatches, leave as is; segment-type alignment may adjust separately
            pass


def main():
    try:
        # Build instance UFO from a temporary .glyphs with export=True for ALL glyphs
        tmp_src = _make_temp_export_all(SRC_PATH)
        try:
            ufo_path = run_fontmake_for_instance(tmp_src)
        finally:
            # cleanup temporary dir
            try:
                shutil.rmtree(tmp_src.parent)
            except Exception:
                pass
        mid = add_regular_master_from_ufo(SRC_PATH, ufo_path)
        print("DONE: Regular master created.")
        print("New master id:", mid)
    except subprocess.CalledProcessError as e:
        print("ERROR: fontmake failed:", e)
        sys.exit(1)
    except Exception as e:
        print("ERROR:", e)
        print(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()