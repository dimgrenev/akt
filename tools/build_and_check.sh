#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "$0")"/.. && pwd)
GLYPHS="$ROOT_DIR/sources/Akt.glyphs"
OUT_TTF="$ROOT_DIR/ofl/akt/Akt[wght].ttf"

python3 -m venv "$ROOT_DIR/.venv"
source "$ROOT_DIR/.venv/bin/activate"
pip install -U pip fontmake gftools fonttools fontbakery shaperglot

fontmake -g "$GLYPHS" -o variable \
  --filter DecomposeTransformedComponentsFilter \
  --filter FlattenComponentsFilter \
  --filter 'DottedCircleFilter(pre=True)' \
  --output-path "$OUT_TTF"

gftools gen-stat "$OUT_TTF" --src "$ROOT_DIR/tools/stat.yaml" --inplace || true

python "$ROOT_DIR/tools/fix_names.py" "$OUT_TTF"

gftools fix-gasp --autofix "$OUT_TTF" || true

python "$ROOT_DIR/tools/write_avar.py" "$OUT_TTF" || true

python "$ROOT_DIR/tools/fix_fvar.py" "$OUT_TTF" || true
python "$ROOT_DIR/tools/fix_prep.py" "$OUT_TTF" || true

fontbakery check-googlefonts "$OUT_TTF" --succinct
