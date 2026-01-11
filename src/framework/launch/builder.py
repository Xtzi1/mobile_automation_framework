from __future__ import annotations

from framework.driver.fake_driver import FakeDriver
from framework.input_layer.gestures import InputLayer
from framework.launch.config import LaunchConfig
from framework.session.context import SessionContext
from ui_tree.driver_bridge import Viewport
from ui_tree.fake_backend import FakeUiTreeBackend


def build_session_context(config: LaunchConfig) -> SessionContext:
    """
    Построить SessionContext для MVP.

    В качестве драйвера используется FakeDriver, а backend ui_tree — FakeUiTreeBackend.

    Параметры:
        config: конфигурация запуска, на основе которой строится контекст.

    Возвращает:
        SessionContext: готовый контекст сессии с драйвером, ui_tree и input layer.
    """

    driver = FakeDriver()
    ui_backend = FakeUiTreeBackend()

    viewport = Viewport(width=1080, height=1920)
    input_layer = InputLayer(driver=driver, viewport=viewport)

    return SessionContext(
        driver=driver,
        ui_tree_backend=ui_backend,
        input_layer=input_layer,
        viewport=viewport,
        config=config
    )
