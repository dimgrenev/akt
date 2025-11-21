#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "$0")"/.. && pwd)
GLYPHS="$ROOT_DIR/sources/Akt.glyphs"
OUT_TTF="$ROOT_DIR/ofl/akt/Akt[wght].ttf"

python3 -m venv "$ROOT_DIR/.venv"
source "$ROOT_DIR/.venv/bin/activate"
pip install -U pip fontmake gftools fonttools fontbakery shaperglot

python "$ROOT_DIR/tools/prepare_union_masters.py" "$GLYPHS" "$OUT_TTF" || fontmake -g "$GLYPHS" -o variable \
  --filter DecomposeTransformedComponentsIFilter \
  --filter DecomposeComponentsIFilter \
  --filter DecomposeComponentsIFilter \
  --filter DecomposeComponentsIFilter \
  --overlaps-backend pathops \
  --filter FlattenComponentsIFilter \
  --filter 'DottedCircleFilter(pre=True)' \
  --output-path "$OUT_TTF"

# Merge overlaps at TT stage to ensure visible union when masters remain incompatible
python "$ROOT_DIR/tools/merge_outlines.py" "$OUT_TTF" || true

gftools gen-stat "$OUT_TTF" --src "$ROOT_DIR/tools/stat.yaml" --inplace || true

python "$ROOT_DIR/tools/fix_names.py" "$OUT_TTF"

gftools fix-gasp --autofix "$OUT_TTF" || true

python "$ROOT_DIR/tools/write_avar.py" "$OUT_TTF" || true

python "$ROOT_DIR/tools/fix_fvar.py" "$OUT_TTF" || true
python "$ROOT_DIR/tools/fix_prep.py" "$OUT_TTF" || true

python "$ROOT_DIR/tools/check_instances.py" "$OUT_TTF" || true
python "$ROOT_DIR/tools/diagnose_masters.py" "$GLYPHS" || true
python "$ROOT_DIR/tools/check_glyph_variation.py" "$OUT_TTF" || true
python "$ROOT_DIR/tools/fix_gasp.py" "$OUT_TTF" || true
.venv/bin/gftools fix-gasp --autofix "$OUT_TTF" || true


fontbakery check-googlefonts "$OUT_TTF" --succinct
