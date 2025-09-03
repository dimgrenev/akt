from youseedee import ucd_data
from pprint import pprint
import sys

char = sys.argv[1]
if len(char) > 1:
  pprint(ucd_data(int(char,16)))
else:
  pprint(ucd_data(ord(char)))