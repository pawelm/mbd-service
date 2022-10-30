from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi import status as status_code
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta

from adapters.out.db.db_connection import create_session
from adapters.out.db.users_repository import UsersRepository
from application.use_case import AuthenticateUserUsecase, GenerateTokenUsecase
from domain.auth import Token
from config import settings

router = APIRouter()


@router.post("/", response_model=Token)
async def auth(form_data: OAuth2PasswordRequestForm = Depends()):
    async with create_session() as dbsession:
        use_case = AuthenticateUserUsecase(UsersRepository(dbsession))
        user = await use_case.execute(
            username=form_data.username, plain_password=form_data.password
        )

        if not user:
            raise HTTPException(status_code=400, detail="Incorrect email or password")

        token_expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_TTL)
        token = await GenerateTokenUsecase().execute(user.id, token_expires_delta)

        return {"access_token": token, "token_type": "bearer"}
