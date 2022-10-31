from typing import List, Optional
import logging

from sqlalchemy.exc import DataError
from sqlalchemy.future import select
from sqlalchemy.sql import Select, desc, distinct, func

from adapters.out.db.base import BaseRepository
from adapters.out.db.models import Post as PostDB
from domain.posts import FetchedPost, FetchPostsQueryParams


logger = logging.getLogger(__name__)


class PostsRepository(BaseRepository):
    async def fetch_posts(self, query_params: FetchPostsQueryParams):
        filters = []
        if query_params.title:
            filters.append(PostDB.title.contains(query_params.title))
        if query_params.start_date:
            filters.append(PostDB.created_at >= query_params.start_date)
        if query_params.end_date:
            filters.append(PostDB.created_at <= query_params.end_date)
        posts = await self._db.execute(select(PostDB).where(*filters))
        result = [FetchedPost(**item.Post.__dict__) for item in posts.mappings()]
        return result


    async def create_post(self, payload):
        post = PostDB(**payload)
        try:
            self._db.add(post)
            await self._db.flush()
            await self._db.refresh(post)
            return post
        except (DataError) as e:
            raise RuntimeError(f"Failed to create Post, {e}")
