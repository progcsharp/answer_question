import pytest
import os
import sys
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch
from httpx import AsyncClient

# Добавляем родительскую директорию в Python path
sys.path.insert(0, str(Path(__file__).parent))

# Загружаем переменные окружения
from dotenv import load_dotenv
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path, override=True)

# Теперь импортируем app
from app import app
from db.engine import get_db

@pytest.fixture
def mock_db_session():
    """Создаем мок сессии базы данных"""
    return AsyncMock()

@pytest.fixture
def override_dependencies(mock_db_session):
    """Переопределяем зависимости базы данных"""
    async def mock_get_db():
        return mock_db_session
    
    app.dependency_overrides[get_db] = mock_get_db
    yield
    app.dependency_overrides.clear()

@pytest.fixture
async def async_client(override_dependencies):
    """Создаем асинхронный HTTP клиент для тестирования"""
    async with AsyncClient(base_url="http://test") as client:
        # Мокируем transport для работы с FastAPI приложением
        from httpx._transports.asgi import ASGITransport
        client._transport = ASGITransport(app=app)
        yield client

# Фикстуры с тестовыми данными
@pytest.fixture
def test_question_data():
    return {"text": "Test question text"}

@pytest.fixture
def test_answer_data():
    return {"text": "Test answer text", "user_id": "test_user"}

@pytest.fixture
def mock_question():
    from datetime import datetime
    from shemas.questions import Question
    return Question(
        id=1,
        text="Test question",
        created_at=datetime.now(),
        answers=[]
    )

@pytest.fixture
def mock_question_with_answers():
    from datetime import datetime
    from shemas.questions import Question
    from shemas.answer import Answer
    return Question(
        id=1,
        text="Test question with answers",
        created_at=datetime.now(),
        answers=[
            Answer(id=1, text="Answer 1", created_at=datetime.now(), question_id=1, user_id="1"),
            Answer(id=2, text="Answer 2", created_at=datetime.now(), question_id=1, user_id="2")
        ]
    )

@pytest.fixture
def mock_answer():
    from datetime import datetime
    from shemas.answer import Answer
    return Answer(
        id=1,
        text="Test answer",
        created_at=datetime.now(),
        question_id=1,
        user_id="1"
    )