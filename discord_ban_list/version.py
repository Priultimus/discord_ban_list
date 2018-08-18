"""versioninfo for discord_ban_list"""


# pylint: disable=too-few-public-methods
class VersionInfo:
    """Version info dataclass"""

    __slots__ = ('major', 'minor', 'build', 'level', 'serial')

    # pylint: disable=too-many-arguments
    def __init__(self, major: int, minor: int, build: int, level: str, serial: int):
        self.major = major
        self.minor = minor
        self.build = build
        self.level = level
        self.serial = serial

    def __str__(self):
        return '{major}.{minor}.{build}{level}{serial}'.format(
            major=self.major,
            minor=self.minor,
            build=self.build,
            level=self.level,
            serial=self.serial,
        )

    def __repr__(self):
        return str(self)


version = VersionInfo(1, 0, 0, 'a', 0)
