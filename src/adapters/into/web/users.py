from fastapi import APIRouter, Depends, Response
from fastapi import status as status_code
from starlette.responses import JSONResponse

from adapters.out.db.db_connection import create_session
from adapters.out.db.users_repository import UsersRepository
from application.use_case import RegisterUserUsecase
from domain.users import User, UserCreate
from utils import get_current_user

router = APIRouter()


@router.post(
    "",
    response_model=User,
    status_code=status_code.HTTP_201_CREATED,
    tags=["users"],
)
async def register_user(user: UserCreate):
    async with create_session() as dbsession:
        use_case = RegisterUserUsecase(UsersRepository(dbsession))
        try:
            result = await use_case.execute(
                {"username": user.name, "password": user.password}
            )
        except RuntimeError:
            return JSONResponse(
                content={"message": "User already exists"}, status_code=400
            )
        else:
            return result


@router.get(
    "",
    response_model=User,
    status_code=status_code.HTTP_200_OK,
    tags=["users"],
)
async def get_user(
    current_user: User = Depends(get_current_user),
):
    return current_user
