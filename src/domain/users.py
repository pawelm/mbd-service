from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str = Field(..., min_length=10)
