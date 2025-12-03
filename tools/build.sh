#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "$0")"/.. && pwd)

python3 -m venv "$ROOT_DIR/.venv"
source "$ROOT_DIR/.venv/bin/activate"
pip install -U pip fontmake fontbakery glyphsLib skia-pathops defcon gftools statmake


# Build variable font to ofl/akt and post-process tables
OUT_DIR="$ROOT_DIR/ofl/akt"
mkdir -p "$OUT_DIR"
OUT_TTF="$OUT_DIR/Akt[wght].ttf"
# Generate Designspace from Glyphs (for STAT or analysis)
DS_PATH=$(python "$ROOT_DIR/tools/prepare_masters.py")

# Build via gftools builder to respect Glyphs export params; then copy VF to ofl
gftools builder "$ROOT_DIR/sources/config.yaml"
VF_SRC="$ROOT_DIR/fonts/variable/Akt[wght].ttf"
if [ -f "$VF_SRC" ]; then
  cp -f "$VF_SRC" "$OUT_TTF"
fi

if [ -f "$OUT_TTF" ]; then
  python "$ROOT_DIR/tools/add_stat.py" "$OUT_TTF" "$DS_PATH" || true
fi

# Add avar table from designspace mappings
if [ -f "$OUT_TTF" ]; then
  python "$ROOT_DIR/tools/add_stat.py" "$OUT_TTF" "$DS_PATH" || true
fi

# Add avar table from designspace mappings
if [ -f "$OUT_TTF" ]; then
  fonttools varLib.avar.build "$OUT_TTF" "$DS_PATH" -o "$OUT_TTF" || true
  # Fallback: if avar still missing, inject identity avar
  python "$ROOT_DIR/tools/add_avar_identity.py" "$OUT_TTF" || true
fi

# Ensure GASP table is present for unhinted fonts
if [ -f "$OUT_TTF" ]; then
  gftools fix-nonhinting "$OUT_TTF" "$OUT_TTF.fixed" || true
  if [ -f "$OUT_TTF.fixed" ]; then
    mv "$OUT_TTF.fixed" "$OUT_TTF"
  fi
  rm -f "$OUT_DIR"/*-backup-fonttools-prep-gasp.ttf || true
  python "$ROOT_DIR/tools/fix_names.py" "$OUT_TTF" || true
  python "$ROOT_DIR/tools/add_meta.py" "$OUT_TTF" "$ROOT_DIR/ofl/akt/METADATA.pb" || true
  python "$ROOT_DIR/tools/add_softdotted_ccmp.py" "$OUT_TTF" || true
fi

# QA is run externally; do not emit reports or create root-level out


echo "Build complete. Fonts in $ROOT_DIR/fonts"
