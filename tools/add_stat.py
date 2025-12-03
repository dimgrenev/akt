#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
from fontTools.otlLib.builder import buildStatTable

def main(ttf_path, _designspace_path):
    tt = TTFont(ttf_path)
    macNames = any(nr.platformID == 1 for nr in getattr(tt.get("name"), "names", ()))
    axes = [
        dict(
            tag="wght",
            name={"en": "Weight"},
            ordering=0,
            values=[
                dict(name={"en": "Thin"}, value=100),
                dict(name={"en": "ExtraLight"}, value=200),
                dict(name={"en": "Light"}, value=300),
                dict(name={"en": "Regular"}, value=400, flags=2),
                dict(name={"en": "Medium"}, value=500),
                dict(name={"en": "SemiBold"}, value=600),
                dict(name={"en": "Bold"}, value=700),
                dict(name={"en": "ExtraBold"}, value=800),
                dict(name={"en": "Black"}, value=900),
            ],
        )
    ]
    buildStatTable(tt, axes, [], 2, macNames=macNames)
    tt.save(ttf_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: add_stat.py <font.ttf> <designspace.designspace>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
