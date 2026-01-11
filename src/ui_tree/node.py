from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class Bounds:
    """Логические границы элемента в координатах сцены приложения."""

    x: float
    y: float
    width: float
    height: float


Predicate = Callable[["Node"], bool]


@dataclass
class Node:
    """Упрощённый узел дерева UI для MVP."""

    id: str
    type: str
    text: Optional[str] = None
    bounds: Optional[Bounds] = None
    attributes: Dict[str, Any] = field(default_factory=dict)
    parent: Optional["Node"] = field(default=None, repr=False)
    children: List["Node"] = field(default_factory=list, repr=False)

    def add_child(self, child: "Node") -> None:
        """
        Добавить дочерний узел к текущему узлу.

        Параметры:
            child: узел, который должен стать потомком текущего.
        """

        child.parent = self
        self.children.append(child)

    def find_first(self, predicate: Predicate) -> Optional["Node"]:
        """
        Найти первый узел, удовлетворяющий предикату.

        Поиск выполняется в глубину, начиная с текущего узла.

        Параметры:
            predicate: функция, получающая узел и возвращающая True, если он подходит.

        Возвращает:
            Первый подходящий узел или None, если ничего не найдено.
        """

        if predicate(self):
            return self

        for child in self.children:
            result = child.find_first(predicate)
            if result is not None:
                return result

        return None

    def find_all(self, predicate: Predicate, result: Optional[List["Node"]] = None) -> List["Node"]:
        """
        Найти все узлы, удовлетворяющие предикату.

        Параметры:
            predicate: функция, получающая узел и возвращающая True, если он подходит.
            result: список для накопления результатов (используется при рекурсии).

        Возвращает:
            Список всех подходящих узлов (включая текущий, если он удовлетворяет предикату).
        """

        if result is None:
            result = []

        if predicate(self):
            result.append(self)

        for child in self.children:
            child.find_all(predicate, result)

        return result
