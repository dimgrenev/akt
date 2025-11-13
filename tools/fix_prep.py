#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._p_r_e_p import table__p_r_e_p
from fontTools.ttLib.tables.ttProgram import Program

def main(path):
    tt = TTFont(path)
    prog = Program()
    # PUSHW 0x01FF; SCANCTRL; PUSHB 0x04; SCANTYPE
    bytecode = [0xB8, 0x01, 0xFF, 0x85, 0xB0, 0x04, 0x8D]
    prog.fromBytecode(bytecode)
    prep = table__p_r_e_p()
    prep.program = prog
    tt['prep'] = prep
    tt.save(path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: fix_prep.py path/to/font.ttf')
        sys.exit(1)
    main(sys.argv[1])

