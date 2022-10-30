import os
import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_CREDENTIALS: str = os.environ["DB_CREDENTIALS"]
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_TTL: int = 60 * 24 * 8
    SECRET_KEY: str = secrets.token_urlsafe(32)


settings = Settings()
