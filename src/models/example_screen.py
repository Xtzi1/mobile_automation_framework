from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from ui_tree.backend import UiTreeBackend
from ui_tree.node import Node


@dataclass
class ExampleScreenModel:
    """
    Пример модели экрана для MVP."""

    backend: UiTreeBackend

    @property
    def root(self) -> Optional[Node]:
        """Корневой узел текущего snapshot-а экрана."""

        return self.backend.get_root()

    @property
    def example_button(self) -> Optional[Node]:
        """
        Узел кнопки example_button, найденный по test_id.

        Возвращает:
            Node или None, если кнопка отсутствует в дереве UI.
        """

        root = self.root
        if root is None:
            return None

        return root.find_first(lambda n: n.attributes.get("test_id") == "example_button")
