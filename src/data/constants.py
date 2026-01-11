from __future__ import annotations

from enum import Enum


class Platform(str, Enum):
    """Поддерживаемые платформы запуска MVP."""

    IOS = "ios"
    ANDROID = "android"


class DeviceProfile(str, Enum):
    """Поддерживаемые профили устройств для MVP."""

    LOCAL = "local"
    REMOTE = "remote"


class LogLevel(str, Enum):
    """Поддерживаемые уровни логирования для MVP."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
