from __future__ import annotations

from dataclasses import dataclass

from framework.driver.interfaces import Driver
from framework.input_layer.gestures import InputLayer
from framework.launch.config import LaunchConfig
from ui_tree.backend import UiTreeBackend
from ui_tree.driver_bridge import Viewport


@dataclass
class SessionContext:
    """
    Контекст тестовой сессии для MVP.

    Содержит всё необходимое для выполнения шагов:
    - драйвер;
    - backend дерева UI;
    - слой ввода;
    - viewport;
    - launch-конфиг.
    """

    driver: Driver
    ui_tree_backend: UiTreeBackend
    input_layer: InputLayer
    viewport: Viewport
    config: LaunchConfig
