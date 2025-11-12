#!env python3
import sys
from argparse import ArgumentParser
from bumpversion.cli import (
    _determine_vcs_dirty,
    _commit_to_vcs,
    _tag_in_vcs,
    _parse_new_version,
)
from bumpversion.utils import ConfiguredFile
from bumpversion.vcs import Git
from bumpversion.version_part import VersionPart, VersionConfig
import logging
import os
from datetime import datetime
from fontTools.designspaceLib import DesignSpaceDocument

from .ufohandler import UFOHandler
from .glyphshandler import GlyphsHandler
from .sfnthandler import SFNTHandler

handlers = [UFOHandler(), GlyphsHandler(), SFNTHandler()]

logging.basicConfig(format="%(name)s %(levelname)s: %(message)s")

logger = logging.getLogger("bump2fontversion")
time_context = {"now": datetime.now(), "utcnow": datetime.utcnow()}
special_char_context = {c: c for c in ("#", ";")}
parser = r"(?P<major>\d+)\.(?P<minor>\d+)"
serializer = "{major}.{minor}"
vc = VersionConfig(parser, [serializer], None, None)


def ufos_from_designspaces(designspaces):
    ufos = []
    for fp in designspaces:
        ds = DesignSpaceDocument()
        ds.read(fp)
        for src in ds.sources:
            ufos.append(src.path)
    return ufos


def main():
    parser = ArgumentParser(description="Bump a font source version")
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        default=False,
        help="Don't write any files, just pretend.",
    )
    parser.add_argument(
        "--verbose",
        "-V",
        action="store_true",
        default=False,
        help="Print verbose logging to stderr.",
    )
    parser.add_argument(
        "--commit",
        action="store_true",
        dest="commit",
        help="Commit to version control",
    )
    parser.add_argument(
        "--tag",
        action="store_true",
        dest="tag",
        help="Create a tag in version control",
    )
    parser.add_argument(
        "--sign-tags",
        action="store_true",
        dest="sign_tags",
        help="Sign tags if created",
    )
    parser.add_argument(
        "--tag-name",
        metavar="TAG_NAME",
        help="Tag name (only works with --tag)",
        default="v{new_version}",
    )
    parser.add_argument(
        "--tag-message",
        metavar="TAG_MESSAGE",
        dest="tag_message",
        help="Tag message",
        default="Bump version: {current_version} → {new_version}",
    )
    parser.add_argument(
        "--message",
        "-m",
        metavar="COMMIT_MSG",
        help="Commit message",
        default="Bump version: {current_version} → {new_version}",
    )
    parser.add_argument(
        "--commit-args",
        metavar="COMMIT_ARGS",
        help="Extra arguments to commit command",
        default="",
    )
    # This interface is slightly different than bump2version (but better!)

    gp = parser.add_mutually_exclusive_group(required=True)
    gp.add_argument(
        "--new-version",
        metavar="VERSION",
        help="New version that should be in the files",
    )
    gp.add_argument(
        "--part", help="Part of the version to be bumped.", choices=["major", "minor"]
    )

    parser.add_argument(
        "files", metavar="file", nargs="*", help="Files to change",
    )
    args = parser.parse_args()
    defaults = {"allow_dirty": True}

    if args.verbose:
        logger.setLevel("INFO")

    print(logger.getEffectiveLevel())

    if not args.files:
        print("No files to change; nothing to do")
        sys.exit(0)

    versions = {}
    new_version = None
    if args.new_version:
        new_version = _parse_new_version(args, None, vc)
        if new_version is None:
            logger.error(f"Bad version {args.new_version}; should be format X.Y")
            sys.exit(1)

    designspaces = [f for f in args.files if f.endswith(".designspace")]
    additional_ufos = ufos_from_designspaces(designspaces)
    if additional_ufos:
        args.files = [
            f for f in args.files if not f.endswith(".designspace")
        ] + additional_ufos

    for f in args.files:
        handled = False
        if not os.path.exists(f):
            logger.warning("%s does not exist, skipping." % f)
            continue

        for h in handlers:
            if not h.applies_to(f):
                continue

            current_version = h.current_version(f)

            if not args.new_version:
                logger.info(
                    f"Current version of {f} is {vc.serialize(current_version, {})}"
                )
                new_version_for_this_file = current_version.bump(
                    args.part, ["major", "minor"]
                )
            else:
                new_version_for_this_file = new_version

            logger.info(
                f"New version of {f} is {vc.serialize(new_version_for_this_file, {})}"
            )
            if not args.dry_run:
                h.set_version(f, new_version_for_this_file)
            versions.setdefault(
                (current_version, new_version_for_this_file), []
            ).append(f)
            handled = True
        if not handled:
            logger.warning("No handler found for file %s, skipping." % f)

    if not args.commit and not args.tag:
        # All done
        sys.exit(0)

    vcs = _determine_vcs_dirty([Git], defaults)
    if vcs:
        for (old_version, new_version), files in versions.items():
            files = [ConfiguredFile(f, True) for f in files]
            args.current_version = vc.serialize(old_version, {})
            args.new_version = vc.serialize(new_version, {})
            context = _commit_to_vcs(
                files, {}, None, False, vcs, args, old_version, new_version,
            )
            _tag_in_vcs(vcs, context, args)


def v_dict(version):
    major, minor = version
    return {"major": VersionPart(major), "minor": VersionPart(minor)}


def bump_part(current, part):
    major, minor = current
    if part == "minor":
        return major, minor + 1
    return major + 1, 0


def verify_version(new_version):
    parts = new_version.split(".")
    if len(parts) != 2:
        return None
    try:
        major, minor = parts
        return int(major), int(minor)
    except Exception:
        return None


if __name__ == "__main__":
    main()
