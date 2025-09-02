from logging.config import fileConfig
import os

from sqlalchemy import create_engine, pool
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

from db.models import Base

from dotenv import load_dotenv

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def get_database_url():
    load_dotenv()
    """Получаем URL базы данных из переменных окружения"""
    db_name = os.getenv("POSTGRES_DB", "fastapi_test")
    db_user = os.getenv("POSTGRES_USER", "postgres")
    db_password = os.getenv("POSTGRES_PASSWORD", "147896325")
    db_host = os.getenv("POSTGRES_HOST", "postgres")
    db_port = os.getenv("POSTGRES_PORT", "5432")
    
    # ИСПОЛЬЗУЕМ СИНХРОННЫЙ ДРАЙВЕР для Alembic
    url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    print(f"Database URL: {url}")
    return url

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = get_database_url()
    
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # Используем синхронный драйвер
    connectable = create_engine(
        get_database_url(),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
