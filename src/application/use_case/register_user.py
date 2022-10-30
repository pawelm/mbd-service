

class RegisterUserUsecase:
    def __init__(self, users_repo):
        self.users_repo = users_repo

    async def execute(self, payload):
        user = await self.users_repo.register_user(payload)
        return user
