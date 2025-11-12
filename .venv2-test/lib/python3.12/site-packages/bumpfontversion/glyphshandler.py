from glyphsLib import GSFont
import logging
from bumpversion.version_part import Version, VersionPart

logger = logging.getLogger(__name__)


class GlyphsHandler:
    def applies_to(self, file):
        return file.endswith(".glyphs")

    def current_version(self, file):
        font = GSFont(file)
        return Version(
            {
                "major": VersionPart(str(font.versionMajor or 0)),
                "minor": VersionPart(str(font.versionMinor or 0)),
            }
        )

    def set_version(self, file, new_version):
        font = GSFont(file)
        font.versionMajor = int(new_version["major"].value)
        font.versionMinor = int(new_version["minor"].value)
        logger.info(f"Saving file {file}")
        font.save(file)
