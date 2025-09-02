from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .config import get_database_config

# Получаем конфигурацию базы данных
db_config = get_database_config()

# Создаем асинхронный движок
engine = create_async_engine(
    db_config.database_url,
    echo=False,
    pool_size=db_config.pool_size,
    max_overflow=db_config.max_overflow
)

# Создаем фабрику сессий
SessionLocal = async_sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine, 
    expire_on_commit=False
    
)


class DBContext:

    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    """Зависимость для получения сессии базы данных"""
    async with SessionLocal() as session:
        try:
            yield session
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
