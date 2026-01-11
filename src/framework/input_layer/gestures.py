from __future__ import annotations

from typing import Tuple

from framework.driver.interfaces import Driver
from ui_tree.driver_bridge import Viewport, logical_bounds_to_screen_point
from ui_tree.node import Bounds


class InputLayer:
    """Слой ввода: исполняет жесты поверх драйвера, используя координаты экрана."""

    def __init__(self, driver: Driver, viewport: Viewport) -> None:
        """
        Создать слой ввода поверх указанного драйвера.

        Параметры:
            driver: объект драйвера, реализующий протокол Driver.
            viewport: описание viewport экрана, в координатах которого работают жесты.
        """

        self._driver = driver
        self._viewport = viewport

    def tap_bounds(self, bounds: Bounds) -> None:
        """
        Выполнить тап по центру указанных логических границ.

        Параметры:
            bounds: логические границы элемента, по которому нужно выполнить тап.
        """

        point = logical_bounds_to_screen_point(bounds, self._viewport)
        self._driver.tap(point)

    def tap_point(self, point: Tuple[int, int]) -> None:
        """
        Выполнить тап по указанной точке экрана.

        Параметры:
            point: координаты точки тапа (x, y).
        """

        self._driver.tap(point)
