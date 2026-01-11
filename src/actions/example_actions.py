from __future__ import annotations

from framework.session.context import SessionContext
from ..models.example_screen import ExampleScreenModel


def tap_example_button(session: SessionContext) -> None:
    """
    Пример бизнес-действия: тап по example_button.

    Параметры:
        session: контекст сессии, содержащий ui_tree backend и слой ввода.
    """

    session.ui_tree_backend.refresh()
    screen = ExampleScreenModel(backend=session.ui_tree_backend)
    button = screen.example_button
    if button is None or button.bounds is None:
        raise AssertionError("example_button is not available in UI tree")

    session.input_layer.tap_bounds(button.bounds)
