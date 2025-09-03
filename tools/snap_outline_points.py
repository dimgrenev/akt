#!/usr/bin/env python3
"""
Snap near-miss outline Y coordinates in a built TTF/OTF font.

This script adjusts on-curve point Y values (and composite component Y offsets)
that are within a small threshold of key vertical metrics so they sit exactly on
those metrics. This helps satisfy FontBakery's outline_alignment_miss check.

- The script reads metrics from the OS/2 table when available:
  * sTypoAscender  -> ascender line
  * sCapHeight     -> cap-height
  * sxHeight       -> x-height
  * sTypoDescender -> descender line (negative)
  Baseline is assumed to be 0.
- If any of those metrics are missing, the following defaults are used:
  baseline=0, x-height=500, cap-height=720, ascender=960, descender=-240.

Usage:
  python3 tools/snap_outline_points.py path/to/font.ttf [--threshold 3] [--dry-run]

Notes:
- Variable fonts are supported (coordinates are adjusted in the default outline).
- For composite glyphs, component y offsets are snapped as well.
- The font file is modified in-place unless --dry-run is provided.
"""
from __future__ import annotations

import argparse
from fontTools.ttLib import TTFont
import math

DEFAULT_METRICS = {
    'baseline': 0,
    'x-height': 500,
    'cap-height': 720,
    'ascender': 960,
    'descender': -240,
}


def load_metrics(tt: TTFont) -> dict:
    m = DEFAULT_METRICS.copy()
    os2 = tt.get('OS/2')
    if os2:
        # Baseline is 0 by convention
        try:
            if getattr(os2, 'sxHeight', 0):
                m['x-height'] = int(getattr(os2, 'sxHeight'))
        except Exception:
            pass
        try:
            if getattr(os2, 'sCapHeight', 0):
                m['cap-height'] = int(getattr(os2, 'sCapHeight'))
        except Exception:
            pass
        try:
            if getattr(os2, 'sTypoAscender', None) is not None:
                m['ascender'] = int(getattr(os2, 'sTypoAscender'))
        except Exception:
            pass
        try:
            if getattr(os2, 'sTypoDescender', None) is not None:
                m['descender'] = int(getattr(os2, 'sTypoDescender'))
        except Exception:
            pass
    return m


def snap_value(y: int, metrics: dict, threshold: int) -> tuple[int, str | None]:
    for name, target in metrics.items():
        if abs(y - target) <= threshold:
            return target, name
    return y, None


def _apply_coords(glyph, glyf, coords):
    # Prefer setCoordinates API when available; otherwise, fallback to direct assignment.
    if hasattr(glyph, 'setCoordinates'):
        try:
            glyph.setCoordinates(coords, glyf)
            return
        except Exception:
            pass
    # Fallback-safe: assign coordinates directly (may not work on very old fontTools)
    try:
        glyph.coordinates = coords
    except Exception:
        # Last resort: do nothing; caller will still recalc bounds if possible
        pass


def _is_oncurve(flag: int) -> bool:
    # TrueType glyf flags bit0 indicates on-curve
    try:
        return bool(flag & 1)
    except Exception:
        return False


def _snap_implicit_midpoints(coords, endPts, flags, metrics: dict, threshold: int) -> int:
    """
    Handle implicit on-curve points in quadratic outlines: whenever two consecutive
    off-curve points occur, there's an implicit on-curve at their midpoint. If that
    midpoint is close to a key metric line, nudge the pair so the midpoint lands
    exactly on the target line. We distribute the integer delta across the pair.
    """
    changed = 0
    if flags is None:
        return 0
    n = len(coords)
    if n == 0:
        return 0

    contour_starts = []
    last_end = -1
    for ep in endPts:
        contour_starts.append(last_end + 1)
        last_end = ep

    used = set()  # indices already adjusted in this pass

    for start, end in zip(contour_starts, endPts):
        # iterate through contour points including wrap-around pair (end, start)
        idxs = list(range(start, end + 1))
        pairs = list(zip(idxs, idxs[1:] + [idxs[0]]))
        for i, j in pairs:
            if i in used or j in used:
                continue
            fi = flags[i] if i < len(flags) else 0
            fj = flags[j] if j < len(flags) else 0
            if _is_oncurve(fi) or _is_oncurve(fj):
                continue
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            # current implicit midpoint Y
            ymid = (float(y1) + float(y2)) / 2.0
            # find nearest target within threshold but not already exact
            best = None
            for line_name, target in metrics.items():
                delta = float(target) - ymid
                if abs(delta) <= threshold and abs(delta) > 0:
                    # prefer smallest |delta|
                    if best is None or abs(delta) < abs(best[0]):
                        best = (delta, target)
            if not best:
                continue
            delta, target = best
            # We need (y1+dy1 + y2+dy2) / 2 == target  =>  dy1 + dy2 == 2*target - (y1+y2)
            S_needed = 2 * int(target)
            S_curr = int(round(y1)) + int(round(y2))
            D = S_needed - S_curr  # integer sum delta
            # distribute D across the pair with minimal movement
            dy1 = int(math.floor(D / 2))
            dy2 = D - dy1
            if abs(dy1) <= threshold and abs(dy2) <= threshold:
                # apply
                coords[i] = (x1, int(round(y1)) + dy1)
                coords[j] = (x2, int(round(y2)) + dy2)
                used.add(i); used.add(j)
                changed += 2
    return changed


def snap_simple_glyph(glyf, glyph, glyph_name: str, metrics: dict, threshold: int) -> int:
    coords_tuple = glyph.getCoordinates(glyf)
    # Support both 2- and 3-tuple returns
    coords = coords_tuple[0]
    endPts = coords_tuple[1] if len(coords_tuple) > 1 else []
    flags = coords_tuple[2] if len(coords_tuple) > 2 else None

    changed = 0
    # 1) Snap explicit points (both on- and off-curve) that are already near lines
    for i in range(len(coords)):
        x, y = coords[i]
        # Snap points more aggressively: try rounded y with threshold
        rounded_y = int(round(y))
        new_y, line = snap_value(rounded_y, metrics, threshold)
        if new_y == rounded_y and abs(rounded_y - y) <= 1:
            # If within 1 unit of integer and that integer is near a metric, align to it
            for _, target in metrics.items():
                if abs(rounded_y - target) <= threshold:
                    new_y = target
                    break
        if new_y != y:
            coords[i] = (x, new_y)
            changed += 1

    # 2) Snap implicit on-curve midpoints created between consecutive off-curves
    changed += _snap_implicit_midpoints(coords, endPts, flags, metrics, threshold)

    if changed:
        _apply_coords(glyph, glyf, coords)
        try:
            glyph.recalcBounds(glyf)
        except Exception:
            pass
    return changed


def _component_transform(comp):
    # Returns affine matrix (a,b,c,d,e,f)
    try:
        t = getattr(comp, 'transform', None)
    except Exception:
        t = None
    if t and len(t) == 6:
        return t
    # Fallback to pure translation if transform is not set
    e = float(getattr(comp, 'x', 0.0))
    f = float(getattr(comp, 'y', 0.0))
    return (1.0, 0.0, 0.0, 1.0, e, f)


def snap_composite_glyph(glyf, glyph, glyph_name: str, metrics: dict, threshold: int, tt: TTFont) -> int:
    changed = 0
    if not hasattr(glyph, 'components') or not glyph.components:
        return 0

    # Build a cache of base glyph coordinates to avoid re-reading multiple times
    glyf_table = glyf
    base_cache = {}

    # Helper: apply affine transform to a point
    def apply_affine(pt, M):
        x, y = pt
        a, b, c, d, e, f = M
        return (a * x + c * y + e, b * x + d * y + f)

    # For each component, look at implicit midpoints in the base glyph as they end up in composite space
    for comp in glyph.components:
        base_name = comp.glyphName
        if base_name not in glyf_table.glyphs:
            continue
        bg = glyf_table[base_name]
        if base_name not in base_cache:
            try:
                coords_tuple = bg.getCoordinates(glyf_table)
                base_cache[base_name] = (bg, coords_tuple)
            except Exception:
                continue
        bg, base_tuple = base_cache[base_name]
        coords_b, endPts_b = base_tuple[0], base_tuple[1]
        flags_b = base_tuple[2] if len(base_tuple) > 2 else None

        M = _component_transform(comp)

        # Pass A: explicit points near metrics (both on- and off-curve) -> suggest integer df to align
        # Group by metric line, then prioritize baseline/cap-height within a strict tolerance
        line_deltas = {}
        strict_line_deltas = {}
        all_deltas = []
        strict_t = min(threshold, 3)
        for idx, (x, y) in enumerate(coords_b):
            # consider only on-curve points for component offset snapping to avoid off-curve noise
            if flags_b is not None:
                fi = flags_b[idx] if idx < len(flags_b) else 0
                if not _is_oncurve(fi):
                    continue
            a, b, c, d, e, f = M
            y_abs = b * float(x) + d * float(y) + float(f)
            for line_name, target in metrics.items():
                delta = float(target) - y_abs
                if abs(delta) <= threshold and abs(delta) > 0:
                    df = int(round(delta))
                    if abs(df) <= threshold:
                        all_deltas.append(df)
                        line_deltas.setdefault(line_name, []).append(df)
                        if abs(delta) <= strict_t:
                            strict_line_deltas.setdefault(line_name, []).append(df)

        def majority_df(items):
            if not items:
                return 0
            from collections import Counter
            cnt = Counter(items)
            # prefer highest frequency, then prefer df=0, then smaller absolute value
            return sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0] != 0, abs(kv[0])))[0][0]

        # choose best_df by maximizing total matches across lines, prefer df=0 then smaller |df|
        best_df = 0
        chosen_line = None
        from collections import Counter
        # Strict counts (<= strict_t)
        strict_counts = Counter()
        for ln, dfs in strict_line_deltas.items():
            strict_counts.update(dfs)
        if strict_counts:
            best_df = sorted(strict_counts.items(), key=lambda kv: (-kv[1], kv[0] != 0, abs(kv[0])))[0][0]
        else:
            counts = Counter()
            for ln, dfs in line_deltas.items():
                counts.update(dfs)
            if counts:
                best_df = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0] != 0, abs(kv[0])))[0][0]

        # If no decision yet, try a tiny baseline-focused nudge based on on-curve points close to baseline
        if best_df == 0:
            small_tol = min(2, threshold)
            baseline_small = []
            for idx, (x, y) in enumerate(coords_b):
                if flags_b is not None:
                    fi = flags_b[idx] if idx < len(flags_b) else 0
                    if not _is_oncurve(fi):
                        continue
                a, b, c, d, e, f = M
                y_abs = b * float(x) + d * float(y) + float(f)
                delta = float(metrics['baseline']) - y_abs
                if 0 < abs(delta) <= small_tol:
                    baseline_small.append(int(round(delta)))
            if baseline_small:
                cnt = Counter(baseline_small)
                best_df = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0] != 0, abs(kv[0])))[0][0]
        # end baseline-focused nudge

        if best_df == 0:
            # Fallback: choose the smallest absolute delta towards baseline/descender if within threshold
            smallest = None  # (abs_delta, df)
            for idx, (x, y) in enumerate(coords_b):
                a, b, c, d, e, f = M
                y_abs = b * float(x) + d * float(y) + float(f)
                for pname in ('baseline', 'descender'):
                    target = metrics[pname]
                    delta = float(target) - y_abs
                    if abs(delta) <= threshold and abs(delta) > 0:
                        df = int(round(delta))
                        cand = (abs(delta), df)
                        if smallest is None or cand[0] < smallest[0]:
                            smallest = cand
            if smallest is not None:
                best_df = smallest[1]
                chosen_line = 'any'

        # Pass B: implicit midpoint .5-fix by adjusting base off-curve pair parity
        # only do this if transform is pure translate/scale without shear (b and c ~ 0)
        parity_changes = 0
        if abs(M[1]) < 1e-6 and abs(M[2]) < 1e-6:
            contour_starts = []
            last_end = -1
            for ep in endPts_b:
                contour_starts.append(last_end + 1)
                last_end = ep
            for start, end in zip(contour_starts, endPts_b):
                idxs = list(range(start, end + 1))
                pairs = list(zip(idxs, idxs[1:] + [idxs[0]]))
                for i, j in pairs:
                    if flags_b is not None:
                        fi = flags_b[i] if i < len(flags_b) else 0
                        fj = flags_b[j] if j < len(flags_b) else 0
                        if _is_oncurve(fi) or _is_oncurve(fj):
                            continue
                    x1, y1 = coords_b[i]
                    x2, y2 = coords_b[j]
                    # current midpoint after transform
                    ymid = (M[3] * float(y1) + M[1] * float(x1) + M[5] + M[3] * float(y2) + M[1] * float(x2) + M[5]) / 2.0
                    # if midpoint sits exactly at .5 away from any metric and within threshold, adjust parity by 1
                    for _, target in metrics.items():
                        delta = float(target) - ymid
                        if abs(delta) <= threshold:
                            frac = abs(delta) - int(abs(delta))
                            # handle .5 parity issues
                            if abs(frac - 0.5) < 1e-6:
                                step = 1 if delta > 0 else -1
                                # nudge one point of the pair by 1 unit in base space
                                coords_b[i] = (x1, int(round(y1)) + step)
                                parity_changes += 1
                                break
            if parity_changes:
                # write back to base glyph and refresh cache
                try:
                    _apply_coords(bg, glyf_table, coords_b)
                    bg.recalcBounds(glyf_table)
                except Exception:
                    pass
                try:
                    coords_tuple = bg.getCoordinates(glyf_table)
                    base_cache[base_name] = (bg, coords_tuple)
                except Exception:
                    pass

        # Pass C: explicit on-curve near-miss snapping in base glyph (no shear), tiny adjustments only
        point_changes = 0
        if abs(M[1]) < 1e-6 and abs(M[2]) < 1e-6:
            d = M[3]
            if abs(d) > 1e-6:
                small_tol = min(2, threshold)
                # Re-fetch possibly updated base coords/flags after Pass B
                coords_b, endPts_b = base_cache[base_name][1][0], base_cache[base_name][1][1]
                flags_b = base_cache[base_name][1][2] if len(base_cache[base_name][1]) > 2 else None
                for i, (x, y) in enumerate(coords_b):
                    if flags_b is not None:
                        fi = flags_b[i] if i < len(flags_b) else 0
                        if not _is_oncurve(fi):
                            continue
                    y_abs = M[1] * float(x) + d * float(y) + M[5]
                    best = None
                    for _, target in metrics.items():
                        delta = float(target) - y_abs
                        if 0 < abs(delta) <= small_tol:
                            if best is None or abs(delta) < abs(best):
                                best = delta
                    if best is None:
                        continue
                    # translate desired delta in composite space to base space
                    dy_base = int(round(best / d))
                    if dy_base != 0 and abs(dy_base) <= small_tol:
                        coords_b[i] = (x, int(round(y)) + dy_base)
                        point_changes += 1
                if point_changes:
                    try:
                        _apply_coords(bg, glyf_table, coords_b)
                        bg.recalcBounds(glyf_table)
                    except Exception:
                        pass
                    try:
                        coords_tuple = bg.getCoordinates(glyf_table)
                        base_cache[base_name] = (bg, coords_tuple)
                    except Exception:
                        pass


        # Apply best_df from explicit points if any
        if best_df != 0:
            try:
                t = getattr(comp, 'transform', None)
                if t and len(t) == 6:
                    a,b,c,d,e,f = t
                    new_t = (a,b,c,d,e, int(round(float(f) + float(best_df))))
                    comp.transform = new_t
                else:
                    current_y = getattr(comp, 'y', 0)
                    comp.y = int(round(float(current_y) + float(best_df)))
                changed += 1
            except Exception:
                pass

    if changed:
        try:
            glyph.recalcBounds(glyf)
        except Exception:
            pass
    return changed


def process_font_report(path: str, threshold: int) -> tuple[int, dict]:
    """Dry-run style processing that returns per-glyph change counts without saving.
    Does a single pass equivalent to process_font() pass logic.
    """
    tt = TTFont(path)
    glyf = tt['glyf']
    metrics = load_metrics(tt)
    total_changes = 0
    per_glyph = {}
    for gname in tt.getGlyphOrder():
        g = glyf[gname]
        if g.isComposite():
            changed = snap_composite_glyph(glyf, g, gname, metrics, threshold, tt)
        else:
            changed = snap_simple_glyph(glyf, g, gname, metrics, threshold)
        if changed:
            total_changes += changed
            per_glyph[gname] = per_glyph.get(gname, 0) + changed
    return total_changes, per_glyph


def process_font(path: str, threshold: int, dry_run: bool = False) -> int:
    tt = TTFont(path)
    glyf = tt['glyf']
    metrics = load_metrics(tt)

    total_changes = 0

    for gname in tt.getGlyphOrder():
        g = glyf[gname]
        if g.isComposite():
            changed = snap_composite_glyph(glyf, g, gname, metrics, threshold, tt)
        else:
            changed = snap_simple_glyph(glyf, g, gname, metrics, threshold)
        if changed:
            total_changes += changed
    if not dry_run and total_changes:
        tt.save(path)
    return total_changes


def main():
    parser = argparse.ArgumentParser(description='Snap near-miss outline points to key metrics, including implicit midpoints and composite adjustments.')
    parser.add_argument('font', help='Path to font file (TTF/OTF)')
    parser.add_argument('--threshold', type=int, default=5, help='Snapping threshold in font units (default: 5)')
    parser.add_argument('--dry-run', action='store_true', help='Do not write changes, only report count')
    parser.add_argument('--max-iterations', type=int, default=2, help='Repeat snapping passes to reach stability (default: 2)')
    parser.add_argument('--report', action='store_true', help='Print per-glyph change counts (analysis only; does not modify the file)')
    args = parser.parse_args()

    if args.report:
        total, per_glyph = process_font_report(args.font, threshold=args.threshold)
        print(f"Total potential changes (single pass): {total}")
        if not per_glyph:
            print("No near-miss outline points detected within threshold.")
            return
        print("\nPer-glyph potential fixes (desc by count):")
        for gname, cnt in sorted(per_glyph.items(), key=lambda x: (-x[1], x[0])):
            print(f"  {gname}: {cnt}")
        return

    total = 0
    for it in range(args.max_iterations):
        changes = process_font(args.font, threshold=args.threshold, dry_run=args.dry_run)
        total += changes
        print(f"Pass {it+1}: changes={changes}")
        if changes == 0:
            break
    print(f"Total changes across passes: {total}")

if __name__ == '__main__':
    main()


def round_half_up(x: float) -> int:
    return int(math.floor(x + 0.5)) if x >= 0 else int(math.ceil(x - 0.5))