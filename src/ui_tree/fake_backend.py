from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from .backend import UiTreeBackend
from .node import Bounds, Node


class FakeUiTreeBackend(UiTreeBackend):
    """Фейковый backend для ui_tree, загружающий snapshot из JSON.

    Используется в unit-тестах и feature-тесте на FakeDriver.
    """

    def __init__(self, snapshot_path: Optional[Path] = None) -> None:
        """
        Создать backend с указанным путём до JSON snapshot-а.

        Параметры:
            snapshot_path: путь к файлу snapshot-а дерева UI.
                Если не указан, используется стандартный пример из config/ui_tree.
        """
        if snapshot_path is None:
            project_root = Path(__file__).resolve().parents[2]
            snapshot_path = project_root / "config" / "ui_tree" / "example_snapshot.json"
        self._snapshot_path = snapshot_path
        self._root: Optional[Node] = None

    def refresh(self) -> None:
        """Загрузить дерево из JSON snapshot-а."""

        data = json.loads(self._snapshot_path.read_text(encoding="utf-8"))
        self._root = self._build_node(data)

    def _build_node(self, data: dict) -> Node:
        """
        Построить объект Node из словаря JSON.

        Параметры:
            data: словарь с описанием узла (id, type, text, bounds, attributes, children).

        Возвращает:
            Экземпляр Node с инициализированными полями и потомками.
        """
        bounds_data = data.get("bounds")
        bounds = None
        if bounds_data is not None:
            bounds = Bounds(
                x=float(bounds_data["x"]),
                y=float(bounds_data["y"]),
                width=float(bounds_data["width"]),
                height=float(bounds_data["height"])
            )

        node = Node(
            id=str(data.get("id", "")),
            type=str(data.get("type", "")),
            text=data.get("text"),
            bounds=bounds,
            attributes=data.get("attributes", {}) or {}
        )

        for child_data in data.get("children", []) or []:
            child = self._build_node(child_data)
            node.add_child(child)

        return node

    def get_root(self) -> Optional[Node]:
        """Вернуть корневой узел текущего snapshot-а."""

        return self._root
