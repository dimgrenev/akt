#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals
import argparse
import openstep_plist
import json
import binascii
import pydoc
from functools import partial
from io import StringIO, open


class BytesEncoder(json.JSONEncoder):
    def default(self, obj):
        from glyphsLib.types import BinaryData

        if isinstance(obj, (bytes, BinaryData)):
            return "<%s>" % binascii.hexlify(obj).decode()
        return json.JSONEncoder.default(self, obj)


def main(args=None):
    if args is None:
        import sys

        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="input file")
    parser.add_argument("outfile", help="output file", default="-", nargs="?")
    parser.add_argument(
        "-g", "--glyphs", help="use glyphsLib parser/writer", action="store_true"
    )
    parser.add_argument(
        "--no-pager", dest="pager", help="do not use pager", action="store_false"
    )
    parser.add_argument(
        "-j", "--json", help="use json to serialize", action="store_true", default=False
    )
    parser.add_argument("-i", "--indent", help="indentation level", type=int, default=2)
    parser.add_argument(
        "--no-escape-newlines", dest="escape_newlines", action="store_false"
    )
    args = parser.parse_args(args)

    if not args.glyphs:
        parse = partial(openstep_plist.load, use_numbers=True)
    else:

        def parse(fp, dict_type=dict):
            from glyphsLib.parser import Parser

            s = fp.read()
            p = Parser(current_type=dict_type)
            return p.parse(s)

    if args.json:
        dump = partial(
            json.dump, cls=BytesEncoder, sort_keys=True, indent=" " * args.indent
        )
    else:
        if args.glyphs:
            from glyphsLib.writer import dump
        else:
            dump = partial(
                openstep_plist.dump,
                indent=args.indent,
                escape_newlines=args.escape_newlines,
            )

    with open(args.infile, "r", encoding="utf-8") as fp:
        data = parse(fp)

    if args.outfile == "-":
        if args.pager:
            buf = StringIO()
            dump(data, buf)
            pydoc.pager(buf.getvalue())
        else:
            dump(data, sys.stdout)
    else:
        with open(args.outfile, "w", encoding="utf-8") as fp:
            dump(data, fp)


if __name__ == "__main__":
    main()
