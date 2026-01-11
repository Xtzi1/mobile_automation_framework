from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from .node import Node


class UiTreeBackend(ABC):
    """Интерфейс backend-а, который предоставляет snapshot дерева UI."""

    @abstractmethod
    def refresh(self) -> None:
        """Обновить snapshot дерева (например, запросом к приложению)."""

    @abstractmethod
    def get_root(self) -> Optional[Node]:
        """Вернуть корневой узел текущего snapshot-а."""
