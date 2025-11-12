import sys
from ttfautohint import run


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    return run(args).returncode


if __name__ == "__main__":
    sys.exit(main())
