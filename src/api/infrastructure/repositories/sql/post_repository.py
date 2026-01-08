from sqlmodel import Session

from api.domain.entities.post import Post
from api.domain.repositories.post import PostRepository
from api.infrastructure.db.models.post import PostModel


class SQLPostRepository(PostRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, post: Post) -> Post:
        model = PostModel(**post.__dict__)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return Post(**model.dict())
