"""Helper APIs for interaction with Google Fonts glyphsets.

Provides APIs to interact with font subsets, codepoints for font or subset.
"""
import codecs
import contextlib
import re
import sys
import warnings
# importlib.resources.files only available since Python>3.9,
# temporarily use backport
from importlib_resources import files
from fontTools import ttLib

from . import subsets

nam_files = files("gfsubsets.data")


class NamFileDict(dict):
    cache = {}

    def __getitem__(self, subset):
        if subset not in self.cache:
            self.cache[subset] = self.read_namfile(subset)
        return self.cache[subset]

    def read_namfile(self, subset):
        cps = set()
        ref = nam_files.joinpath(subset + "_unique-glyphs.nam")
        if not ref.is_file():
            warnings.warn(f"No such subset '{subset}'")
            return cps
        with ref.open("r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                match = _NAMELIST_CODEPOINT_REGEX.match(line[2:7])
                if match is not None:
                    cps.add(int(match.groups()[0], 16))
        return cps


subset_codepoints = NamFileDict()

# Matches 4 or 5 hexadecimal digits that are uppercase at the beginning of the
# test string. The match is stored in group 0, e.g:
# >>> _NAMELIST_CODEPOINT_REGEX.match('1234X').groups()[0]
# '1234'
# >>> _NAMELIST_CODEPOINT_REGEX.match('1234A').groups()[0]
# '1234A'
_NAMELIST_CODEPOINT_REGEX = re.compile("^([A-F0-9]{4,5})")

_PLATFORM_ID_MICROSOFT = 3
_PLATFORM_ENC_UNICODE_BMP = 1
_PLATFORM_ENC_UNICODE_UCS4 = 10
_PLATFORM_ENCS_UNICODE = (_PLATFORM_ENC_UNICODE_BMP, _PLATFORM_ENC_UNICODE_UCS4)


def UnicodeCmapTables(font):
    """Find unicode cmap tables in font.

    Args:
      font: A TTFont.
    Yields:
      cmap tables that contain unicode mappings
    """
    for table in font["cmap"].tables:
        if (
            table.platformID == _PLATFORM_ID_MICROSOFT
            and table.platEncID in _PLATFORM_ENCS_UNICODE
        ):
            yield table


def CodepointsInFont(font_filename):
    """Returns the set of codepoints present in the font file specified.

    Args:
      font_filename: The name of a font file.
    Returns:
      A set of integers, each representing a codepoint present in font.
    """

    font_cps = set()
    with contextlib.closing(ttLib.TTFont(font_filename)) as font:
        for t in UnicodeCmapTables(font):
            font_cps.update(t.cmap.keys())

    return font_cps


def ListSubsets():
    """Returns a list of all subset names, in lowercase."""
    return subsets.SUBSETS


def SubsetsForCodepoint(cp):
    """Returns all the subsets that contains cp or [].

    Args:
      cp: int codepoint.
    Returns:
      List of lowercase names of subsets or [] if none match.
    """
    _subsets = []
    for subset in ListSubsets():
        cps = CodepointsInSubset(subset, unique_glyphs=True)
        if not cps:
            continue
        if cp in cps:
            _subsets.append(subset)
    return _subsets


def SubsetForCodepoint(cp):
    """Returns the highest priority subset that contains cp or None.

    Args:
      cp: int codepoint.
    Returns:
      The lowercase name of the subset, e.g. latin, or None.
    """
    _subsets = SubsetsForCodepoint(cp)
    if not _subsets:
        return None

    result = _subsets[0]
    for subset in sorted(_subsets):
        # prefer x to x-ext
        if result + "-ext" == subset:
            pass
        elif result == subset + "-ext":
            # prefer no -ext to -ext
            result = subset
        elif subset.startswith("latin"):
            # prefer latin to anything non-latin
            result = subset

    return result


def set_encoding_path(enc_path):
    raise NotImplementedError("set_encoding_path is no longer supported")


def CodepointsInSubset(subset, unique_glyphs=False):
    """Returns the set of codepoints contained in a given subset.

    Args:
      subset: The lowercase name of a subset, e.g. latin.
      unique_glyphs: Optional, whether to only include glyphs unique to subset.
    Returns:
      A set containing the glyphs in the subset.
    """
    cps = subset_codepoints[subset]

    if unique_glyphs:
        return cps

    # y-ext includes y
    # Except latin-ext which already has latin.
    if subset != "latin-ext" and subset.endswith("-ext"):
        cps |= subset_codepoints[subset[:-4]]

    # almost all subsets include latin.
    if subset not in ("khmer", "latin"):
        cps |= subset_codepoints["latin"]
    return cps


def SubsetsInFont(file_path, min_pct, ext_min_pct=None):
    """Finds all subsets for which we support > min_pct of codepoints.

    Args:
      file_path: A file_path to a font file.
      min_pct: Min percent coverage to report a subset. 0 means at least 1 glyph.
      25 means 25%.
      ext_min_pct: The minimum percent coverage to report a -ext
      subset supported. Used to admit extended subsets with a lower percent. Same
      interpretation as min_pct. If None same as min_pct.
    Returns:
      A list of 3-tuples of (subset name, #supported, #in subset).
    """
    all_cps = CodepointsInFont(file_path)
    # Remove control chars and whitespace chars from the font since they may
    # trigger greek-ext and latin-ext subsets to be enabled.
    # https://github.com/googlefonts/nam-files/issues/14#issuecomment-2076693612
    for codepoint in set([0x0000, 0x000D, 0x0020, 0x00A0]):
        if codepoint in all_cps:
            all_cps.remove(codepoint)

    results = []
    for subset in ListSubsets():
        subset_cps = CodepointsInSubset(subset, unique_glyphs=True)
        if not subset_cps:
            continue

        # Khmer includes latin but we only want to report support for non-Latin.
        if subset == "khmer":
            subset_cps -= CodepointsInSubset("latin")

        overlap = all_cps & subset_cps

        target_pct = min_pct
        if ext_min_pct is not None and subset.endswith("-ext"):
            target_pct = ext_min_pct

        if 100.0 * len(overlap) / len(subset_cps) > target_pct:
            results.append((subset, len(overlap), len(subset_cps)))

    return results
