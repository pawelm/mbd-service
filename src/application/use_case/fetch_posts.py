class FetchPostsUsecase:
    def __init__(self, posts_repo):
        self.posts_repo = posts_repo

    async def execute(self, query_params):
        post = await self.posts_repo.fetch_posts(query_params)
        return post
