from __future__ import annotations

from framework.launch.builder import build_session_context
from framework.launch.config import LaunchConfig
from framework.session.context import SessionContext


def build_session(config: LaunchConfig) -> SessionContext:
    """
    Упрощённый директор, orchestration вокруг builder-а.

    В MVP просто делегирует создание `SessionContext` builder-у.
    """

    return build_session_context(config)
