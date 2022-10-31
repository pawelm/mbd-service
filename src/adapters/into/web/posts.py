from fastapi import APIRouter, Depends, Response
from fastapi import status as status_code

from adapters.out.db.db_connection import create_session
from adapters.out.db.posts_repository import PostsRepository
from application.use_case import CreatePostUsecase, FetchPostsUsecase
from domain.posts import Post, PostCreate, FetchedPosts, FetchPostsQueryParams
from domain.users import User
from utils import get_current_user

router = APIRouter()


@router.post(
    "",
    response_model=Post,
    status_code=status_code.HTTP_201_CREATED,
    tags=["posts"],
)
async def create_post(
    post: PostCreate,
    current_user: User = Depends(get_current_user),
):
    async with create_session() as dbsession:
        use_case = CreatePostUsecase(PostsRepository(dbsession))
        result = await use_case.execute(
            {"title": post.title, "content": post.content, "author_id": current_user.id}
        )
        return result


@router.get(
    "",
    response_model=FetchedPosts,
    status_code=status_code.HTTP_200_OK,
    tags=["posts"],
)
async def fetch_posts(
    query_params: FetchPostsQueryParams = Depends(),
    current_user: User = Depends(get_current_user),
):
    async with create_session() as dbsession:
        use_case = FetchPostsUsecase(PostsRepository(dbsession))
        result = await use_case.execute(query_params)
        return result
