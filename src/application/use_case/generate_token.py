from datetime import timedelta
from typing import Any, Union

from utils import create_access_token


class GenerateTokenUsecase:
    async def execute(self, subject: Union[str, Any], expires_delta: timedelta = None):
        return create_access_token(subject, expires_delta)
