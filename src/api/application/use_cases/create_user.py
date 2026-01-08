from datetime import datetime, timezone

from api.domain.entities.user import User
from api.domain.repositories.user import UserRepository


class CreateUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, name: str) -> User:
        current_time = datetime.now(timezone.utc)

        user = User(
            id=None,
            name=name,
            created=current_time,
            updated=current_time,
        )
        return self.repository.create(user)
