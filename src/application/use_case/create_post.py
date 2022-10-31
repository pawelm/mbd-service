class CreatePostUsecase:
    def __init__(self, posts_repo):
        self.posts_repo = posts_repo

    async def execute(self, payload):
        post = await self.posts_repo.create_post(payload)
        return post
