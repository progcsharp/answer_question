# Question-Answer API

FastAPI приложение для управления вопросами и ответами с асинхронной базой данных PostgreSQL.

## 🚀 Быстрый старт

### 1. Клонирование проекта
```bash
git clone <repository-url>
cd question_test
```

### 2. Создание .env файла
Создайте файл `app/.env` с переменными окружения (см. пример в `app/.env.example`)

### 3. Запуск через Docker Compose
```bash
docker-compose --env-file app/.env up -d
```

### 4. Проверка работы
- API: http://localhost:8080
- Документация: http://localhost:8080/docs
- Health check: http://localhost:8080/health

## 📚 Документация

Подробная документация по запуску, настройке и использованию находится в [app/README.md](app/README.md)

## 🧪 Тестирование

```bash
cd app
python run_tests.py
```

## 🏗️ Архитектура

- **FastAPI** - веб-фреймворк
- **SQLAlchemy** - ORM для работы с БД
- **PostgreSQL** - база данных
- **Docker** - контейнеризация
- **Pytest** - тестирование

## 📁 Структура проекта

```
question_test/
├── README.md                           # Основная документация проекта
├── docker-compose.yml                  # Docker Compose конфигурация
├── nginx.conf                          # Nginx конфигурация
└── app/                                # Основное приложение
```

```
app/
├── app.py                              # Главное FastAPI приложение
├── requirements.txt                     # Зависимости Python
├── pytest.ini                          # Конфигурация pytest
├── run_tests.py                        # Скрипт для запуска тестов
├── README.md                           # Детальная документация app
├── Dockerfile                          # Docker образ для FastAPI
├── alembic/                            # Миграции базы данных
│   ├── env.py                          # Конфигурация Alembic
│   ├── script.py.mako                  # Шаблон для миграций
│   ├── README                          # Документация Alembic
│   └── versions/                       # Файлы миграций
│       └── 4f66f74a7d1f_initial_migration.py
├── db/                                 # Работа с базой данных
│   ├── __init__.py                     # Инициализация пакета
│   ├── config.py                       # Конфигурация БД
│   ├── connection.py                   # Подключение к БД
│   ├── engine.py                       # Движок БД и сессии
│   ├── enums.py                        # Перечисления
│   ├── models.py                       # Модели SQLAlchemy
│   ├── utils.py                        # Утилиты для БД
│   └── handler/                        # Обработчики БД
│       ├── __init__.py                 # Инициализация пакета
│       ├── create.py                   # Создание записей
│       ├── delete.py                   # Удаление записей
│       ├── get.py                      # Получение записей
│       └── update.py                   # Обновление записей
├── exception/                          # Обработка исключений
│   ├── __init__.py                     # Инициализация пакета
│   └── database.py                     # Исключения БД
├── routers/                            # API роутеры
│   ├── __init__.py                     # Инициализация пакета
│   ├── questions.py                    # Роутер для вопросов
│   └── answer.py                       # Роутер для ответов
├── shemas/                             # Pydantic схемы (примечание: должно быть "schemas")
│   ├── __init__.py                     # Инициализация пакета
│   ├── questions.py                    # Схемы вопросов
│   └── answer.py                       # Схемы ответов
└── tests/                              # Тесты
    ├── __init__.py                     # Инициализация пакета
    ├── conftest.py                     # Конфигурация pytest
    ├── test_simple.py                  # Простые тесты приложения
    └── test_validation.py              # Тесты валидации
```

## 🔧 Технологии

- **Backend**: FastAPI, SQLAlchemy
- **Database**: PostgreSQL
- **Testing**: Pytest, pytest-asyncio
- **Containerization**: Docker, Docker Compose
- **Reverse Proxy**: Nginx

## 📝 Лицензия

Этот проект создан в качестве тестового задания для собеседования.
