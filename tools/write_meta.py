#!/usr/bin/env python3
"""
Write META table with dlng/slng tags to a TTF/OTF.
Usage: python tools/write_meta.py fonts/Akt[wght].ttf
"""
import argparse
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._m_e_t_a import table__m_e_t_a

DLNG = "Latn,Cyrl"
SLNG = "Latn,Cyrl"


def write_meta(font_path: str):
    font = TTFont(font_path)
    meta = table__m_e_t_a("meta")
    meta.data = {}
    meta.data["dlng"] = DLNG
    meta.data["slng"] = SLNG
    font["meta"] = meta
    font.save(font_path)
    print(f"Injected META table (dlng='{DLNG}', slng='{SLNG}') into {font_path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("font_path", help="Path to font file (TTF/OTF)")
    args = ap.parse_args()
    write_meta(args.font_path)