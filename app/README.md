# Question-Answer API

FastAPI приложение для управления вопросами и ответами с асинхронной базой данных PostgreSQL.

## 🚀 Запуск проекта

### Вариант 1: Запуск через Docker Compose (рекомендуется)

#### 1. Создание файла .env

Перед запуском создайте файл `.env` в папке `app` со следующим содержимым:

```bash
DATABASE_URL=postgresql+asyncpg://myuser:mypassword@postgres:5432/mydatabase
DB_HOST=postgres
DB_PORT=5432
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
```

#### 2. Запуск через Docker Compose

Передайте путь к файлу .env через флаг `--env-file`:

```bash
# Из корневой директории проекта
docker-compose --env-file app/.env up -d
```

#### 3. Проверка работы

После запуска API будет доступен по адресу:
- **API**: http://localhost:8080
- **Документация**: http://localhost:8080/docs
- **Health check**: http://localhost:8080/health

### Вариант 2: Запуск без Docker (локально)

#### 1. Установка зависимостей

```bash
cd app
pip install -r requirements.txt
```

#### 2. Настройка базы данных

Убедитесь, что у вас установлен и запущен PostgreSQL, или измените `DATABASE_URL` в `.env` на локальный:

```bash
# Для локального PostgreSQL
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/database_name
```

#### 3. Запуск через uvicorn

```bash
cd app
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

## 🧪 Запуск тестов

### Установка зависимостей для тестирования

```bash
cd app
pip install -r requirements.txt
```

### Запуск тестов

```bash
# Все тесты
python -m pytest tests/ -v

# Конкретный тест
python -m pytest tests/test_simple.py::test_app_structure -v

# С выводом print
python -m pytest tests/ -v -s

# Через скрипт
python run_tests.py
```

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
├── 📁 db/                                 # Работа с базой данных
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

## 🔧 API Endpoints

### Questions
- `GET /questions/` - Получить все вопросы
- `GET /questions/{id}` - Получить вопрос по ID
- `POST /questions/` - Создать новый вопрос
- `DELETE /questions/{id}` - Удалить вопрос
- `POST /questions/{id}/answers/` - Добавить ответ к вопросу

### Answers
- `GET /answers/{id}` - Получить ответ по ID
- `DELETE /answers/{id}` - Удалить ответ

### Health
- `GET /health` - Проверка состояния сервиса

## 🐳 Docker команды

```bash
# Запуск
docker-compose --env-file app/.env up -d

# Остановка
docker-compose down

# Просмотр логов
docker-compose logs -f

# Пересборка
docker-compose --env-file app/.env up -d --build

# Очистка
docker-compose down -v --remove-orphans
```
