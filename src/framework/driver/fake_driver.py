from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class FakeDriverCall:
    """Запись вызова к FakeDriver."""

    method: str
    args: Tuple[int, int]
    extra: Tuple[int, int] | None = None


@dataclass
class FakeDriver:
    """Простой драйвер для MVP, который только записывает вызовы."""

    calls: List[FakeDriverCall] = field(default_factory=list)

    def tap(self, point: Tuple[int, int]) -> None:
        """Симулировать тап, записав вызов в историю.

        Параметры:
            point: координаты точки тапа (x, y).
        """

        self.calls.append(FakeDriverCall(method="tap", args=point))

    def swipe(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
        Симулировать свайп, записав вызов в историю.

        Параметры:
            start: координаты начала жеста (x, y).
            end: координаты конца жеста (x, y).
        """

        self.calls.append(FakeDriverCall(method="swipe", args=start, extra=end))
