## Mobile Automation Framework MVP

Минимальный pet-проект, иллюстрирующий архитектуру фреймворка автотестов для мобильного приложения.
Полное архитектурное описание лежит в `docs/`:

- `docs/architecture.md` — общая архитектура и слои;
- `docs/abstraction_layers.md` — уровни абстракции и их тестирование;
- `docs/launch_flow.md` — поток запуска и фикстуры pytest.

### Структура проекта

- `src/framework` — инфраструктура (драйвер, launch, session, input layer);
- `src/ui_tree` — логическое дерево UI и преобразование координат;
- `src/models` — пример UI-модели экрана;
- `src/actions` — пример бизнес-действия;
- `src/tests/unit` — unit-тесты инфраструктуры и ui_tree;
- `src/tests/features` — пример smoke-теста поверх полного стека;
- `config` — JSON-конфиги платформ/девайсов и env.

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск тестов

- Все тесты:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest
```

- Только unit-тесты:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest src/tests/unit
```

- Smoke-сценарии:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest src/tests/features -m "smoke"
```

Доступны CLI-опции (см. `conftest.py`):

- `--platform` — платформа (по умолчанию `ios`);
- `--device-profile` — профиль девайса (по умолчанию `local`);
- `--mvp-log-level` — уровень логирования фреймворка (по умолчанию `INFO`).
