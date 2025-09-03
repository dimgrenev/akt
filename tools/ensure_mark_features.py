#!/usr/bin/env python3
import sys
from pathlib import Path

try:
    import glyphsLib
except Exception as e:
    print(f"[ERROR] glyphsLib not available: {e}")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources" / "Akt.glyphs"


def main():
    if not SRC.exists():
        print(f"[ERROR] Source file not found: {SRC}")
        sys.exit(1)

    font = glyphsLib.GSFont(str(SRC))

    to_remove = {"mark", "mkmk"}
    kept = []
    removed = []

    # glyphsLib GSFeature uses .name for tag
    new_features = []
    for f in list(font.features):
        tag = getattr(f, "name", None) or getattr(f, "tag", None)
        if tag in to_remove:
            removed.append(tag)
            # skip adding to new_features
        else:
            new_features.append(f)
            if tag:
                kept.append(tag)

    if removed:
        font.features = new_features
        font.save(str(SRC))
        print("Removed features:", ", ".join(sorted(set(removed))))
    else:
        print("No 'mark'/'mkmk' features found to remove.")

    if kept:
        print("Kept other features:", ", ".join(sorted(set(kept))))


if __name__ == "__main__":
    main()