from utils import verify_password


class AuthenticateUserUsecase:
    def __init__(self, users_repo):
        self.users_repo = users_repo

    async def execute(self, username, plain_password):
        user = await self.users_repo.get_user_by_name(username)
        if not user:
            return None
        user = user[0]
        if not verify_password(plain_password, user.password):
            return None
        return user
