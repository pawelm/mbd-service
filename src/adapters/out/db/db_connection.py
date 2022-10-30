import json
import logging

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config import settings


logger = logging.getLogger(__file__)


def form_db_connection_string(db_credentials: str) -> str:
    db_creds = json.loads(db_credentials)
    hostname = db_creds["host"]
    user = db_creds["username"]
    pw = db_creds["password"]
    port = db_creds["port"]
    db_name = db_creds["dbname"]
    logger.info(
        f"Connection to db. Details: user:{user}, hostname:{hostname}, port:{port}, db_name:{db_name}"
    )
    return f"postgresql+asyncpg://{user}:{pw}@{hostname}:{port}/{db_name}"


def get_connection_string() -> str:
    return form_db_connection_string(settings.DB_CREDENTIALS)


engine = create_async_engine(get_connection_string())


def create_session() -> AsyncSession:
    engine = create_async_engine(get_connection_string())
    session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    return session.begin()
