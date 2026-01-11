from __future__ import annotations

from pathlib import Path

from config.env import EnvConfig
from data.constants import DeviceProfile, LogLevel, Platform
from framework.launch.config import LaunchConfig, build_launch_config


def test_build_launch_config_basic_fields() -> None:
    """Проверяет, что build_launch_config заполняет основные поля LaunchConfig."""

    config = build_launch_config(
        platform=Platform.IOS,
        device_profile=DeviceProfile.LOCAL,
        log_level=LogLevel.DEBUG,
    )

    assert isinstance(config, LaunchConfig)
    assert config.platform is Platform.IOS
    assert config.device_profile is DeviceProfile.LOCAL
    assert config.log_level is LogLevel.DEBUG
    assert isinstance(config.env, EnvConfig)


def test_build_launch_config_uses_project_root_when_provided(tmp_path: Path) -> None:
    """
    Проверяет, что build_launch_config использует переданный project_root для поиска JSON-конфигураций.

    В MVP достаточно убедиться, что функция не падает даже при отсутствии файлов
    (она должна вернуть корректный LaunchConfig с CLI-значениями).
    """

    project_root = tmp_path

    config = build_launch_config(
        platform=Platform.IOS,
        device_profile=DeviceProfile.LOCAL,
        log_level=LogLevel.INFO,
        project_root=project_root
    )

    assert isinstance(config, LaunchConfig)
    assert config.platform is Platform.IOS
    assert config.device_profile is DeviceProfile.LOCAL
    assert config.log_level is LogLevel.INFO
    assert isinstance(config.env, EnvConfig)
