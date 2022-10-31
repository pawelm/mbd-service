import os
import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_CREDENTIALS: str = os.environ["DB_CREDENTIALS"]
    ACCESS_TOKEN_TTL: int = 60 * 24
    SECRET_KEY: str = secrets.token_urlsafe(32)


settings = Settings()
