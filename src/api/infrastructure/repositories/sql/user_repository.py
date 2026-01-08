from sqlmodel import Session

from api.domain.entities.user import User
from api.domain.repositories.user import UserRepository
from api.infrastructure.db.models.user import UserModel


class SQLUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        model = UserModel(**user.__dict__)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return User(**model.dict())
