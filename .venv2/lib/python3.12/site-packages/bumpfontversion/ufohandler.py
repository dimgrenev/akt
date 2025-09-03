import ufoLib2
import logging
from bumpversion.version_part import Version, VersionPart

logger = logging.getLogger(__name__)


class UFOHandler:
    def applies_to(self, file):
        return file.endswith(".ufo")

    def current_version(self, file):
        font = ufoLib2.objects.Font.open(file)
        return Version(
            {
                "major": VersionPart(str(font.info.versionMajor or 0)),
                "minor": VersionPart(str(font.info.versionMinor or 0)),
            }
        )

    def set_version(self, file, new_version):
        font = ufoLib2.objects.Font.open(file)
        font.info.versionMajor = int(new_version["major"].value)
        font.info.versionMinor = int(new_version["minor"].value)
        logger.info(f"Saving file {file}")
        font.save(file, overwrite=True)
