#!/usr/bin/env python3
import sys, os, tempfile, subprocess
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
import shutil

def ttx_roundtrip(path):
    td = tempfile.mkdtemp()
    ttx_bin = shutil.which("ttx") or os.path.join(os.path.dirname(os.path.dirname(__file__)), ".venv", "bin", "ttx")
    ttx = subprocess.run([ttx_bin, "-o", os.path.join(td, "font.ttx"), path], capture_output=True)
    if ttx.returncode != 0:
        return False, ttx.stderr.decode("utf-8", "ignore")
    back = subprocess.run([ttx_bin, "-o", os.path.join(td, "font.ttf"), os.path.join(td, "font.ttx")], capture_output=True)
    if back.returncode != 0:
        return False, back.stderr.decode("utf-8", "ignore")
    return True, ""

def main(font_path):
    tt = TTFont(font_path)
    weights = [100,200,300,400,500,600,700,800,900]
    failures = []
    for w in weights:
        try:
            inst = instantiateVariableFont(tt, {"wght": float(w)})
            td = tempfile.mkdtemp()
            out = os.path.join(td, f"Akt-{w}.ttf")
            inst.save(out)
            ok, msg = ttx_roundtrip(out)
            if not ok:
                failures.append((w, msg))
            else:
                print(f"OK wght={w}")
        except Exception as e:
            failures.append((w, str(e)))
    if failures:
        print("FAILURES:")
        for w,msg in failures:
            print(f"wght={w}: {msg}")
        return 1
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: check_instances.py path/to/variable.ttf")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
