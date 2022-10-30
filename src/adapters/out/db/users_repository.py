from typing import List, Optional
import logging

from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy.future import select
from sqlalchemy.sql import Select, desc, distinct, func

from adapters.out.db.base import BaseRepository
from adapters.out.db.models import User as UserDB
from domain.users import User


logger = logging.getLogger(__name__)


class UsersRepository(BaseRepository):
    async def get_user_by_name(self, username):
        user = await self._db.execute(select(UserDB).where(UserDB.name == username))
        return user.fetchone()

    async def get_user_by_id(self, user_id):
        user = await self._db.execute(select(UserDB).where(UserDB.id == user_id))
        return user.fetchone()

    async def register_user(self, payload):
        user = UserDB(name=payload["username"], password=payload["password"])
        try:
            self._db.add(user)
            await self._db.flush()
            await self._db.refresh(user)
            return User(id=user.id, name=user.name)
        except (IntegrityError, DataError) as e:
            raise RuntimeError(f"Failed to register User, {e}")
