"""
Конфигурация базы данных
"""
import os
from functools import lru_cache

from dotenv import load_dotenv


class DatabaseConfig:
    """Конфигурация для подключения к базе данных"""
    
    def __init__(self):
        load_dotenv()
        # Получаем URL базы данных из переменной окружения или используем значение по умолчанию
        self.database_url = os.getenv(
            "DATABASE_URL", 
            "postgresql+asyncpg://postgres:147896325@localhost/fastapi_test"
        )
        
        # Настройки пула соединений
        self.pool_size = int(os.getenv("DB_POOL_SIZE", "20"))
        self.max_overflow = int(os.getenv("DB_MAX_OVERFLOW", "0"))
        self.echo = os.getenv("DB_ECHO", "True").lower() == "true"
        


@lru_cache()
def get_database_config() -> DatabaseConfig:
    """Получить конфигурацию базы данных (с кешированием)"""
    return DatabaseConfig()
