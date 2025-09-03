from fontTools.ttLib import TTFont
from fontTools.varLib.instancer.names import _fontVersion, NameID
import logging
import re
from bumpversion.version_part import Version, VersionPart

logger = logging.getLogger(__name__)


class SFNTHandler:
    def applies_to(self, file):
        return file.endswith((".ttf", ".otf", ".woff", ".woff2"))

    def current_version(self, file):
        font = TTFont(file)
        current = _fontVersion(font)
        major, minor = current.split(".")
        return Version(
            {
                "major": VersionPart(str(major or 0)),
                "minor": VersionPart(str(minor or 0)),
            }
        )

    def set_version(self, file, new_version):
        font = TTFont(file)

        minor = new_version['minor'].value
        minor = minor.zfill(3) if int(minor) < 10 else minor
        major = new_version['major'].value

        version_string = f"{major}.{minor}"
        font["head"].fontRevision = float(version_string)

        current_version = _fontVersion(font)
        nametbl = font["name"]
        for rec in nametbl.names:
            if rec.nameID not in [NameID.VERSION_STRING, NameID.UNIQUE_FONT_IDENTIFIER]:
                logger.debug(
                    f"Skipping ({rec.nameID}, {rec.platformID}, {rec.platEncID}, {rec.langID}): "
                    f"{rec.toUnicode()}"
                )
                continue
            new_string = re.sub(current_version, version_string, rec.toUnicode())
            logger.info(
                f"Updating ({rec.nameID}, {rec.platformID}, {rec.platEncID}, {rec.langID}): "
                f"{rec.toUnicode()} --> {new_string}"
            )
            nametbl.setName(new_string, rec.nameID, rec.platformID, rec.platEncID, rec.langID)

        logger.info(f"Saving file {file}")
        font.save(file)
