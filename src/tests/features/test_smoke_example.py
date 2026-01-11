from __future__ import annotations

from typing import cast

import pytest

from framework.driver.fake_driver import FakeDriver
from framework.session.context import SessionContext
from ...actions.example_actions import tap_example_button

EXPECTED_TAP_COUNT = 1
EXPECTED_METHOD_NAME = "tap"


@pytest.mark.smoke
def test_smoke_example_button_tap(session_context: SessionContext) -> None:
    """
    Проверяет, что бизнес-действие выполняет один тап по example_button.

    Параметры:
        session_context: контекст сессии, предоставленный фикстурой.
    """

    tap_example_button(session_context)

    driver = cast(FakeDriver, session_context.driver)
    calls = driver.calls
    assert len(calls) == EXPECTED_TAP_COUNT
    assert calls[0].method == EXPECTED_METHOD_NAME
