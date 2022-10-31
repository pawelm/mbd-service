from typing import Dict, Optional

from fastapi import Depends, FastAPI, Response
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from adapters.into.web.auth import router as auth_router
from adapters.into.web.users import router as users_router
from adapters.into.web.posts import router as posts_router

app = FastAPI(title="MBD Service")

@app.get("/")
async def index():
    return Response(
        content="Welcome to MBD Service API, go to \docs to learn how to use it."
    )

app.include_router(auth_router, prefix="/auth")
app.include_router(users_router, prefix="/user")
app.include_router(posts_router, prefix="/post")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    message = str(exc).replace("field required", "is a required property")
    return JSONResponse(content={"message": message}, status_code=400)
