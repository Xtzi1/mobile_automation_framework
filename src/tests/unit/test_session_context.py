from __future__ import annotations

from data.constants import DeviceProfile, LogLevel, Platform
from framework.driver.fake_driver import FakeDriver
from framework.input_layer.gestures import InputLayer
from framework.launch.config import LaunchConfig, build_launch_config
from framework.launch.director import build_session
from framework.session.context import SessionContext
from ui_tree.backend import UiTreeBackend


def _make_launch_config() -> LaunchConfig:
    return build_launch_config(
        platform=Platform.IOS,
        device_profile=DeviceProfile.LOCAL,
        log_level=LogLevel.INFO
    )


def test_build_session_returns_session_context() -> None:
    """Проверяет, что build_session возвращает корректный SessionContext."""

    launch_config = _make_launch_config()

    session = build_session(launch_config)

    assert isinstance(session, SessionContext)
    assert session.config is launch_config


def test_session_context_components_types() -> None:
    """Проверяет, что SessionContext содержит ожидаемые компоненты инфраструктуры."""

    launch_config = _make_launch_config()

    session = build_session(launch_config)

    assert isinstance(session.driver, FakeDriver)
    assert isinstance(session.ui_tree_backend, UiTreeBackend)
    assert isinstance(session.input_layer, InputLayer)
    assert session.viewport.width > 0
    assert session.viewport.height > 0
