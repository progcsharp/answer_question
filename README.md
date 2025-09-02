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
├── app/                   # Основное приложение
│   ├── app.py            # FastAPI приложение
│   ├── routers/          # API роутеры
│   ├── db/               # Работа с БД
│   ├── shemas/           # Pydantic схемы
│   ├── tests/            # Тесты
│   └── docker-compose.yml
├── nginx/                 # Nginx конфигурация
└── README.md             # Этот файл
```

## 🔧 Технологии

- **Backend**: FastAPI, SQLAlchemy, asyncpg
- **Database**: PostgreSQL
- **Testing**: Pytest, pytest-asyncio
- **Containerization**: Docker, Docker Compose
- **Reverse Proxy**: Nginx

## 📝 Лицензия

Этот проект создан в качестве тестового задания для собеседования.
