#!/usr/bin/env python3
from fontTools.ttLib import TTFont, newTable
import sys
from pathlib import Path

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

def ensure_regular_naming(font: TTFont, family: str, style: str):
    # Family/Style
    set_name_string(font, 1, family)
    set_name_string(font, 2, style)
    set_name_string(font, 4, f"{family} {style}")
    ps = f"{family}-{style}".replace(" ", "")
    set_name_string(font, 6, ps)
    # Version strings
    # NameID 3: Unique font identifier must start with "Version X.XXX;"
    set_name_string(font, 3, "Version 1.000;Akt;Akt-Regular")
    set_name_string(font, 5, "Version 1.000")

def ensure_ofl_license(font: TTFont):
    # Google Fonts requires NameID 13 to be a single-line statement, no line breaks
    set_name_string(font, 13, "This Font Software is licensed under the SIL Open Font License, Version 1.1.")
    # Canonical URL
    set_name_string(font, 14, "https://openfontlicense.org")

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
    # Ensure Regular strings exist
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

def main(path: str):
    font = TTFont(path)
    ensure_regular_naming(font, family="Akt", style="Regular")
    ensure_ofl_license(font)
    ensure_head_revision(font, "1.000")
    ensure_fsselection_regular(font)
    ensure_macstyle_regular(font)
    ensure_fvar_defaults(font)
    ensure_avar(font)
    ensure_meta(font)
    remove_typographic_family_names(font)
    font.save(path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: fix_vf.py path/to/variable.ttf")
        sys.exit(2)
    main(sys.argv[1])


