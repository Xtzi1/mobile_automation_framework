from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class EnvConfig:
    """
    Простая обёртка над переменными окружения для MVP.

    В реальном проекте здесь могут быть адреса backend-сервисов, токены и т.д.
    """

    backend_url: str


def load_env() -> EnvConfig:
    """
    Загрузить конфигурацию окружения для MVP.

    Возвращает:
        EnvConfig: объект с параметрами окружения, необходимыми фреймворку.
    """

    backend_url = os.getenv("MOBILE_AUTOMATION_BACKEND_URL", "http://localhost:8000")

    return EnvConfig(backend_url=backend_url)
