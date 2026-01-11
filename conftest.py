from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterator

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from data.constants import DeviceProfile, LogLevel, Platform
from framework.launch.config import LaunchConfig, build_launch_config
from framework.launch.director import build_session
from framework.session.context import SessionContext

PLATFORM_OPTION = "--platform"
DEVICE_PROFILE_OPTION = "--device-profile"
MVP_LOG_LEVEL_OPTION = "--mvp-log-level"


def pytest_addoption(parser: pytest.Parser) -> None:
    """
    Добавить CLI-опции для управления запуском MVP фреймворка.

    Параметры:
        parser: объект парсера pytest, в который добавляются опции.
    """

    group = parser.getgroup("mobile-automation-framework")
    group.addoption(
        PLATFORM_OPTION,
        default=Platform.IOS.value,
        help="Target platform for mobile automation framework MVP (ios|android)."
    )
    group.addoption(
        DEVICE_PROFILE_OPTION,
        default=DeviceProfile.LOCAL.value,
        help="Device profile name (e.g. local|remote)."
    )
    group.addoption(
        MVP_LOG_LEVEL_OPTION,
        default=LogLevel.INFO.value,
        help="Log level for MVP framework (отдельно от встроенного pytest --log-level)."
    )


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Корневая директория pet-проекта mobile_automation_framework."""

    return PROJECT_ROOT


@pytest.fixture(scope="session")
def launch_config(request: pytest.FixtureRequest, project_root: Path) -> LaunchConfig:
    """
    Собрать LaunchConfig из CLI-опций, env и JSON-конфигов.

    Параметры:
        request: объект запроса pytest, содержащий доступ к опциям.
        project_root: корень проекта, откуда читаются конфиги.

    Возвращает:
        LaunchConfig: конфигурация запуска для текущей тестовой сессии.
    """

    platform_name = str(request.config.getoption(PLATFORM_OPTION))
    device_profile_name = str(request.config.getoption(DEVICE_PROFILE_OPTION))
    log_level_name = str(request.config.getoption(MVP_LOG_LEVEL_OPTION))

    platform = Platform(platform_name)
    device_profile = DeviceProfile(device_profile_name)
    log_level = LogLevel(log_level_name)

    return build_launch_config(
        platform=platform,
        device_profile=device_profile,
        log_level=log_level,
        project_root=project_root
    )


@pytest.fixture(scope="session")
def session_context(launch_config: LaunchConfig) -> SessionContext:
    """
    Создать и вернуть общий SessionContext для тестовой сессии.

    Параметры:
        launch_config: конфигурация запуска, на основе которой строится контекст.

    Возвращает:
        SessionContext: контекст сессии с драйвером, ui_tree и input layer.
    """

    return build_session(launch_config)


@pytest.fixture(scope="function")
def app_session(session_context: SessionContext) -> Iterator[SessionContext]:
    """
    Фикстура для обновления ui_tree перед каждым тестом.

    Параметры:
        session_context: общий контекст сессии, созданный на уровне session.

    Возвращает:
        Итератор, предоставляющий актуальный SessionContext для теста.
    """

    session_context.ui_tree_backend.refresh()
    yield session_context
