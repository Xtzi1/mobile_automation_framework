from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from .node import Bounds


@dataclass(frozen=True)
class Viewport:
    """Простое описание viewport экрана."""

    width: int
    height: int


def logical_bounds_to_screen_point(bounds: Bounds, viewport: Viewport) -> Tuple[int, int]:
    """
    Пересчитать логические bounds в координаты точки на экране.

    В MVP реализуем простое вычисление центра прямоугольника без учёта safe-area и scale.

    Параметры:
        bounds: логические границы элемента в координатах сцены.
        viewport: описание viewport экрана, в координатах которого интерпретируются bounds.

    Возвращает:
        Кортеж (x, y) с координатами точки на экране.
    """

    center_x = bounds.x + bounds.width / 2.0
    center_y = bounds.y + bounds.height / 2.0

    # В MVP считаем, что логические координаты уже в системе viewport.
    return int(center_x), int(center_y)
