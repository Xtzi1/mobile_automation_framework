from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from config.env import EnvConfig, load_env
from data.constants import DeviceProfile, LogLevel, Platform


@dataclass(frozen=True)
class LaunchConfig:
    """Упрощённый launch-конфиг для MVP.

    Поля:
        platform: целевая платформа (например, Platform.IOS / Platform.ANDROID).
        device_profile: профиль устройства (например, DeviceProfile.LOCAL / DeviceProfile.REMOTE).
        log_level: уровень логирования (LogLevel; может быть проброшен дальше в реальный logger).
        env: объект с параметрами окружения.
    """

    platform: Platform
    device_profile: DeviceProfile
    log_level: LogLevel
    env: EnvConfig


def build_launch_config(platform: Platform,
                        device_profile: DeviceProfile,
                        log_level: LogLevel,
                        project_root: Path | None = None) -> LaunchConfig:
    """
    Собрать LaunchConfig из JSON-конфигураций, окружения и CLI-параметров.

    В MVP JSON-файлы используются только как источник имён/профилей,
    а значения CLI имеют приоритет.

    Параметры:
        platform: имя платформы (ios|android и т.п.).
        device_profile: имя профиля устройства (local|remote и т.п.).
        log_level: уровень логирования для запуска.
        project_root: корень проекта, откуда читаются конфиги (если None, определяется автоматически).

    Возвращает:
        LaunchConfig: сборная конфигурация запуска.
    """

    if project_root is None:
        project_root = Path(__file__).resolve().parents[3]

    platforms_dir = project_root / "config" / "platforms"
    devices_dir = project_root / "config" / "devices"

    platforms_config = _load_json(platforms_dir / f"{platform.value}.json")
    devices_config = _load_json(devices_dir / f"{device_profile.value}.json")

    _ = platforms_config, devices_config

    env = load_env()

    return LaunchConfig(
        platform=platform,
        device_profile=device_profile,
        log_level=log_level,
        env=env
    )


def _load_json(path: Path) -> dict:
    """
    Загрузить JSON-файл по указанному пути.

    Параметры:
        path: путь к JSON-файлу.

    Возвращает:
        dict: содержимое файла или пустой словарь, если файл отсутствует.
    """

    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))
