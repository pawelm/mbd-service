from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str


class Post(PostBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class FetchedPost(BaseModel):
    title: str
    content: str
    created_at: datetime


class FetchedPosts(BaseModel):
    __root__: List[FetchedPost]


class FetchPostsQueryParams(BaseModel):
    title: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None