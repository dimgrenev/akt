#!/usr/bin/env python3
from fontTools.ttLib import TTFont, newTable
import sys
from pathlib import Path
from typing import List, Dict, Any
import unicodedata


def set_name_string(font: TTFont, nameID: int, string: str, langID=0x409):
    name = font["name"]
    # Windows Unicode
    name.setName(string, nameID, 3, 1, langID)
    # Mac Roman (fallback)
    try:
        name.setName(string, nameID, 1, 0, 0)
    except Exception:
        pass
    # Unicode platform record (platform 0) to keep all in sync
    try:
        name.setName(string, nameID, 0, 4, 0)
    except Exception:
        # Some writer versions use encID 3; try that as well
        try:
            name.setName(string, nameID, 0, 3, 0)
        except Exception:
            pass

def set_name_multiplatform(font: TTFont, nameID: int, string: str):
    # Helper: write on all common platforms
    set_name_string(font, nameID, string, 0x409)  # Windows en-US
    try:
        font["name"].setName(string, nameID, 1, 0, 0)
    except Exception:
        pass
    try:
        font["name"].setName(string, nameID, 0, 4, 0)
    except Exception:
        pass

def ensure_regular_naming(font: TTFont, family: str, style: str):
    # Стандарт GF для VF: Subfamily = Regular, Full = "Family Regular", PS = "Family-Regular"
    subfamily = "Regular"
    set_name_string(font, 1, family)
    set_name_string(font, 2, subfamily)
    set_name_string(font, 4, f"{family} {subfamily}")
    ps = f"{family}-{subfamily}".replace(" ", "")
    set_name_string(font, 6, ps)

    # Обновим NameID3 (Unique) в формате "Version X.XXX;Family;PS"
    try:
        rev = float(font["head"].fontRevision)
    except Exception:
        rev = 1.0
    unique = f"Version {rev:.3f};{family};{ps}"
    set_name_string(font, 3, unique)
    # Version strings
    # NameID 3: Unique font identifier must start with "Version X.XXX;"
    set_name_string(font, 3, "Version 1.000;Akt;Akt-Regular")
    set_name_string(font, 5, "Version 1.000")

def ensure_copyright_from_ofl(font: TTFont):
    # Set nameID 0 from the first line of OFL.txt to align with FB expectations
    try:
        ofl_text = Path("OFL.txt").read_text(encoding="utf-8").splitlines()
        first_line = ofl_text[0].strip()
        if first_line:
            set_name_multiplatform(font, 0, first_line)
    except Exception:
        # fallback minimal copyright if file missing
        set_name_multiplatform(font, 0, "Copyright 2025 The Akt Project Authors")

def ensure_ofl_license(font: TTFont):
    # Google Fonts requires a specific one-line snippet including the FAQ URL for NameID 13
    snippet = (
        "This Font Software is licensed under the SIL Open Font License, Version 1.1. "
        "This license is available with a FAQ at: https://openfontlicense.org"
    )
    set_name_multiplatform(font, 13, snippet)
    # Canonical URL for NameID 14
    set_name_multiplatform(font, 14, "https://openfontlicense.org")

def ensure_designer_info(font: TTFont):
    # nameID 9: Designer; nameID 12: Designer URL
    set_name_multiplatform(font, 9, "Dmitry Grenev")
    set_name_multiplatform(font, 12, "https://grenev.com")

def ensure_head_revision(font: TTFont, version_str: str = "1.000"):
    try:
        rev = float(version_str)
    except Exception:
        rev = 1.0
    head = font["head"]
    if abs(getattr(head, "fontRevision", 0.0) - rev) > 1e-6:
        head.fontRevision = rev

def remove_typographic_family_names(font: TTFont):
    # Remove NameID 16 and 17 completely (GF expects N/A for variable fonts)
    name = font["name"]
    records = [nr for nr in name.names if nr.nameID not in (16, 17)]
    name.names = records

def ensure_fsselection_regular(font: TTFont):
    os2 = font["OS/2"]
    # Set usWeightClass to 400 for default
    os2.usWeightClass = 400
    # fsSelection: set REGULAR bit (bit 6), clear BOLD (bit 5) and ITALIC (bit 0)
    fs = os2.fsSelection
    # clear bits
    fs &= ~(1 << 5)  # BOLD off
    fs &= ~(1 << 0)  # ITALIC off
    # set REGULAR
    fs |= (1 << 6)
    os2.fsSelection = fs

def ensure_vendor_id(font: TTFont, vendor: str = "NONE"):
    os2 = font["OS/2"]
    try:
        # achVendID is a 4-byte string
        os2.achVendID = vendor[:4].ljust(4)  # pad to 4 chars
    except Exception:
        pass

def ensure_macstyle_regular(font: TTFont):
    head = font["head"]
    # clear Bold (bit 0) and Italic (bit 1)
    head.macStyle &= ~0b11

def ensure_avar(font: TTFont):
    # Create a neutral avar if missing
    if "avar" not in font:
        avar = newTable("avar")
        avar.segments = {}
        # Try to infer axes from fvar
        if "fvar" in font:
            for axis in font["fvar"].axes:
                tag = axis.axisTag
                # neutral mapping: -1:-1, 0:0, 1:1
                avar.segments[tag] = { -1.0: -1.0, 0.0: 0.0, 1.0: 1.0 }
        font["avar"] = avar

def ensure_meta(font: TTFont):
    # Minimal META with design/supported languages
    # Build table object directly with string values
    if "meta" not in font:
        meta = newTable("meta")
    else:
        meta = font["meta"]
    # meta data maps: tag -> string; fontTools will encode on compile
    meta.data = {"dlng": "latn,cyrl", "slng": "latn,cyrl"}
    font["meta"] = meta

def ensure_fvar_defaults(font: TTFont):
    if "fvar" not in font:
        return
    fvar = font["fvar"]
    # Normalize weight axis defaults
    for axis in fvar.axes:
        if axis.axisTag == "wght":
            axis.minValue = 100.0
            axis.defaultValue = 400.0
            # preserve axis.maxValue if larger than 900; otherwise clamp
            axis.maxValue = max(axis.maxValue, 900.0)
    # Point default named instance (if present) to Regular names
    # Find or create nameIDs
    name = font["name"]
    # Ensure default subfamily/PS strings exist per GF standard (Regular)
    set_name_string(font, 2, "Regular")
    set_name_string(font, 6, "Akt-Regular")
    regular_name_id = 2
    regular_ps_id = 6
    # Update instances whose coords equal defaults
    # Compute defaults map
    defaults = {ax.axisTag: ax.defaultValue for ax in fvar.axes}
    for inst in fvar.instances:
        # inst.coordinates: list of axis values aligned to fvar.axes order in older fontTools;
        # recent fontTools exposes .coordinates as dict. Handle both.
        coords = {}
        try:
            coords = inst.coordinates
        except AttributeError:
            # Older versions: build dict from axes order and inst.coordinates list
            values = getattr(inst, "coordinates", None)
            if isinstance(values, (list, tuple)):
                coords = {ax.axisTag: values[i] for i, ax in enumerate(fvar.axes)}
        if not coords:
            continue
        is_default = all(abs(coords.get(tag, defaults[tag]) - defaults[tag]) < 0.001 for tag in defaults)
        if is_default:
            inst.subfamilyNameID = regular_name_id
            # Some fontTools NamedInstance accept postscriptNameID attribute
            try:
                inst.postscriptNameID = regular_ps_id
            except Exception:
                pass

def enforce_regular_naming(font: TTFont, family: str = "Akt") -> None:
    """Force NameIDs 2/4/6/3 to GF standard Regular scheme across all platforms."""
    name = font["name"]
    # remove existing conflicting records
    name.names = [nr for nr in name.names if nr.nameID not in (2, 3, 4, 6)]
    subfamily = "Regular"
    full = f"{family} {subfamily}"
    ps = f"{family}-{subfamily}".replace(" ", "")
    # set across common platforms
    for (pid, eid, lid) in [(3,1,0x409), (1,0,0), (0,4,0)]:
        name.setName(subfamily, 2, pid, eid, lid)
        name.setName(full, 4, pid, eid, lid)
        name.setName(ps, 6, pid, eid, lid)
    # Unique ID
    try:
        rev = float(font["head"].fontRevision)
    except Exception:
        rev = 1.0
    unique = f"Version {rev:.3f};{family};{ps}"
    for (pid, eid, lid) in [(3,1,0x409), (1,0,0), (0,4,0)]:
        name.setName(unique, 3, pid, eid, lid)

def ensure_stat_weight_axis_value_names(font: TTFont) -> None:
    """Ensure STAT AxisValue for wght=700 uses the Bold nameID, not Regular.
    This fixes cases where a generator mislabeled 700 with NameID 2 (Regular)."""
    if "STAT" not in font:
        return
    try:
        stat_table = font["STAT"].table
    except Exception:
        return

    # Find Bold subfamily nameID from fvar named instances (coord wght=700)
    bold_name_id = None
    try:
        fvar = font["fvar"]
        axes = [ax.axisTag for ax in fvar.axes]
        for inst in fvar.instances:
            coords = {}
            try:
                coords = inst.coordinates  # dict in recent fontTools
            except AttributeError:
                values = getattr(inst, "coordinates", None)
                if isinstance(values, (list, tuple)):
                    coords = {axes[i]: values[i] for i in range(min(len(values), len(axes)))}
            w = coords.get("wght")
            if w is not None and abs(float(w) - 700.0) < 0.01:
                bold_name_id = getattr(inst, "subfamilyNameID", None)
                if bold_name_id is not None:
                    bold_name_id = int(bold_name_id)
                    break
    except Exception:
        pass

    if not bold_name_id:
        return

    # Fix AxisValue records for weight axis at value 700
    try:
        axis_values = getattr(stat_table.AxisValueArray, "AxisValue", [])
    except Exception:
        axis_values = []
    for av in axis_values:
        try:
            axis_index = av.AxisIndex
            value = float(av.Value)
        except Exception:
            continue
        if axis_index == 0 and abs(value - 700.0) < 0.01:
            # Overwrite ValueNameID with Bold's subfamily nameID
            try:
                av.ValueNameID = bold_name_id
            except Exception:
                continue

def _glyph_is_letter(font: TTFont, glyph_name: str) -> bool:
    # Determine if glyph maps to any Unicode codepoint with category starting with 'L'
    try:
        cmap = font.getBestCmap() or {}
        # invert: glyph -> list cps
        cps = [cp for cp, g in cmap.items() if g == glyph_name]
        if not cps:
            return False
        for cp in cps:
            if unicodedata.category(chr(cp)).startswith("L"):
                return True
        return False
    except Exception:
        return False


def prune_mark_to_base_non_letters(font: TTFont) -> None:
    """Remove MarkToBase BaseCoverage entries for glyphs that are not Unicode letters.
    Оставляем позиционирование диакритики только на буквах; цифры/знаки/символы исключаем.
    """
    if "GPOS" not in font:
        return
    try:
        gpos = font["GPOS"].table
        lookups = getattr(gpos, "LookupList", None)
        if not lookups or not getattr(lookups, "Lookup", None):
            return
    except Exception:
        return

    for lookup in lookups.Lookup:
        try:
            if int(getattr(lookup, "LookupType", 0)) != 4:
                continue
            for sub in getattr(lookup, "SubTable", []) or []:
                cov = getattr(sub, "BaseCoverage", None)
                base_array = getattr(sub, "BaseArray", None)
                if not cov or not base_array:
                    continue
                glyphs = list(getattr(cov, "glyphs", []) or [])
                if not glyphs:
                    continue
                for i in range(len(glyphs) - 1, -1, -1):
                    g = glyphs[i]
                    if not _glyph_is_letter(font, g):
                        try:
                            cov.glyphs.pop(i)
                            try:
                                base_array.BaseRecord.pop(i)
                            except Exception:
                                pass
                        except Exception:
                            continue
        except Exception:
            continue

def ensure_soft_dotted_decomposition(font: TTFont) -> None:
    """Ensure precomposed soft-dotted forms decompose to dotless base + combining mark.
    This helps FB soft_dotted by guaranteeing dot removal for precomposed i/j.
    """
    if "GSUB" not in font:
        return
    try:
        gsub = font["GSUB"].table
        lookups = getattr(gsub, "LookupList", None)
        if not lookups or not getattr(lookups, "Lookup", None):
            return
    except Exception:
        return

    # Map of precomposed -> [decomposed sequence]
    decomp_map: Dict[str, List[str]] = {
        # i + above marks
        "iacute": ["dotlessi", "acutecomb"],
        "igrave": ["dotlessi", "gravecomb"],
        "icircumflex": ["dotlessi", "uni0302"],
        "idieresis": ["dotlessi", "uni0308"],
        "itilde": ["dotlessi", "tildecomb"],
        "imacron": ["dotlessi", "uni0304"],
        "ibreve": ["dotlessi", "uni0306"],
        # j forms (dotless j is uni0237 in this font)
        "jcircumflex": ["uni0237", "uni0302"],
        "jcaron": ["uni0237", "uni030C"],
    }

    glyph_order = set(font.getGlyphOrder())
    # Find a MultipleSubst lookup to append to; prefer existing ccmp MultipleSubst
    target_lookup = None
    for lk in lookups.Lookup:
        try:
            if int(getattr(lk, "LookupType", 0)) == 2:
                target_lookup = lk
                break
        except Exception:
            continue
    if target_lookup is None:
        return

    try:
        subtables = getattr(target_lookup, "SubTable", []) or []
        if not subtables:
            return
        msub = subtables[0]
        # msub.mapping is a dict glyph->list
        mapping: Dict[str, List[str]] = getattr(msub, "mapping", {})
    except Exception:
        return

    changed = False
    for src, dst_seq in decomp_map.items():
        if src not in glyph_order:
            continue
        # ensure all dst glyphs exist
        if not all(d in glyph_order for d in dst_seq):
            continue
        if mapping.get(src) != dst_seq:
            mapping[src] = dst_seq
            changed = True
    if changed:
        setattr(msub, "mapping", mapping)

def prune_mark_to_base_for(font: TTFont, glyphs_to_remove: list[str]) -> None:
    """Удаляет указанные глифы из BaseCoverage/BaseArray во всех MarkToBase lookup-ах GPOS."""
    if "GPOS" not in font:
        return
    try:
        gpos = font["GPOS"].table
        lookups = getattr(gpos, "LookupList", None)
        if not lookups or not getattr(lookups, "Lookup", None):
            return
    except Exception:
        return
    targets = set(glyphs_to_remove or [])
    for lookup in lookups.Lookup:
        try:
            if int(getattr(lookup, "LookupType", 0)) != 4:
                continue
            for sub in getattr(lookup, "SubTable", []) or []:
                cov = getattr(sub, "BaseCoverage", None)
                base_array = getattr(sub, "BaseArray", None)
                if not cov or not base_array:
                    continue
                glyphs = list(getattr(cov, "glyphs", []) or [])
                if not glyphs:
                    continue
                for i in range(len(glyphs) - 1, -1, -1):
                    if glyphs[i] in targets:
                        try:
                            cov.glyphs.pop(i)
                            try:
                                base_array.BaseRecord.pop(i)
                            except Exception:
                                pass
                        except Exception:
                            continue
        except Exception:
            continue

def main(path: str):
    font = TTFont(path)
    ensure_regular_naming(font, family="Akt", style="Regular")
    ensure_copyright_from_ofl(font)
    ensure_ofl_license(font)
    ensure_head_revision(font, "1.000")
    ensure_designer_info(font)
    ensure_fsselection_regular(font)
    ensure_macstyle_regular(font)
    ensure_fvar_defaults(font)
    ensure_avar(font)
    ensure_meta(font)
    ensure_vendor_id(font, "DMGR")
    remove_typographic_family_names(font)
    enforce_regular_naming(font, family="Akt")
    ensure_stat_weight_axis_value_names(font)
    prune_mark_to_base_for(font, ["copyright", "registered", "uni00A9", "uni00AE"]) 
    ensure_soft_dotted_decomposition(font)
    prune_mark_to_base_non_letters(font)
    font.save(path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: fix_vf.py path/to/variable.ttf")
        sys.exit(2)
    main(sys.argv[1])


