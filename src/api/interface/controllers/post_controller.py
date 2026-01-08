from api.application.use_cases.create_post import CreatePostUseCase


class PostController:
    def __init__(self, use_case: CreatePostUseCase):
        self.use_case = use_case

    def create(self, title: str, content: str, user_id: int):
        return self.use_case.execute(
            title=title,
            content=content,
            user_id=user_id,
        )
