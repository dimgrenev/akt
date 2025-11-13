#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_a_s_p import table__g_a_s_p

def main(path):
    tt = TTFont(path)
    gasp = table__g_a_s_p()
    # 65535: apply to all sizes; value 15 enables gridfit + smoothing flags
    gasp.gaspRange = {65535: 15}
    tt['gasp'] = gasp
    tt.save(path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: fix_gasp.py path/to/font.ttf')
        sys.exit(1)
    main(sys.argv[1])

