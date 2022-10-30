from typing import Optional
from pydantic import BaseModel
from .base import Entity


class UserBase(BaseModel):
    name: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
