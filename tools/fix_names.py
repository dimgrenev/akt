#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont

def set_name(tt, nameID, string):
    # Windows
    tt['name'].removeNames(nameID=nameID, platformID=3, platEncID=1, langID=0x409)
    tt['name'].setName(string, nameID, 3, 1, 0x409)
    # Mac
    tt['name'].removeNames(nameID=nameID, platformID=1, platEncID=0, langID=0)
    tt['name'].setName(string, nameID, 1, 0, 0)

def main(path):
    tt = TTFont(path)
    set_name(tt, 1, 'Akt')
    set_name(tt, 2, 'Regular')
    set_name(tt, 4, 'Akt Regular')
    set_name(tt, 6, 'Akt-Regular')
    set_name(tt, 13, 'This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://openfontlicense.org')
    set_name(tt, 14, 'https://openfontlicense.org')
    tt.save(path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: fix_names.py path/to/font.ttf')
        sys.exit(1)
    main(sys.argv[1])
