from abc import ABC, abstractmethod

from api.domain.entities.post import Post


class PostRepository(ABC):
    @abstractmethod
    def create(self, post: Post) -> Post:
        pass
