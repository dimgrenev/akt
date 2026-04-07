#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "$0")"/.. && pwd)

if [ "$#" -eq 0 ]; then
  exec make -C "$ROOT_DIR" build
fi

exec make -C "$ROOT_DIR" "$@"
