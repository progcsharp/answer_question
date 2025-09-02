# Тестирование Question-Answer API

## Обзор

Этот проект содержит набор тестов для проверки функциональности Question-Answer API, построенного на FastAPI.

## Структура тестов

### Простые тесты (`tests/test_simple.py`)
- **test_app_structure** - проверяет структуру приложения и наличие основных роутов
- **test_health_endpoint_exists** - проверяет наличие health check эндпоинта
- **test_cors_middleware** - проверяет настройку CORS middleware


## Запуск тестов

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск всех тестов
```bash
python -m pytest tests/ -v
```

### Запуск конкретного теста
```bash
python -m pytest tests/test_simple.py::test_app_structure -v
```

### Запуск с выводом print
```bash
python -m pytest tests/ -v -s
```