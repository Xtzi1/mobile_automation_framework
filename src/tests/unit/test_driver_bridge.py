from ui_tree.driver_bridge import Viewport, logical_bounds_to_screen_point
from ui_tree.node import Bounds


def test_logical_bounds_to_screen_point_center() -> None:
    """Проверяет вычисление центра bounds в координаты точки экрана."""

    bounds = Bounds(x=100.0, y=200.0, width=50.0, height=30.0)
    viewport = Viewport(width=1080, height=1920)

    x, y = logical_bounds_to_screen_point(bounds, viewport)

    assert (x, y) == (125, 215)


def test_logical_bounds_to_screen_point_different_offset() -> None:
    """Проверяет вычисление центра для bounds с другим размером и позицией."""

    bounds = Bounds(x=0.0, y=0.0, width=10.0, height=10.0)
    viewport = Viewport(width=100, height=100)

    x, y = logical_bounds_to_screen_point(bounds, viewport)

    assert (x, y) == (5, 5)
