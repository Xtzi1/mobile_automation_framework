from __future__ import annotations

from typing import Protocol, Tuple


class Driver(Protocol):
    """Протокол драйвера для input layer."""

    def tap(self, point: Tuple[int, int]) -> None:
        """
        Выполнить одиночный тап в указанной точке экрана.

        Параметры:
            point: кортеж (x, y) с координатами точки тапа.
        """

    def swipe(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
        Выполнить свайп от одной точки к другой.

        Параметры:
            start: кортеж (x, y) с координатами начала жеста.
            end: кортеж (x, y) с координатами конца жеста.
        """
