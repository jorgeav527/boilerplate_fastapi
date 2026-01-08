from datetime import datetime, timezone

from api.domain.entities.post import Post
from api.domain.repositories.post import PostRepository


class CreatePostUseCase:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def execute(self, title: str, content: str, user_id: int) -> Post:
        current_time = datetime.now(timezone.utc)

        post = Post(
            id=None,
            title=title,
            content=content,
            user_id=user_id,
            created=current_time,
            updated=current_time,
        )
        return self.repository.create(post)
