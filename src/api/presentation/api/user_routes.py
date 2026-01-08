from fastapi import APIRouter, Depends
from sqlmodel import Session

from api.application.use_cases.create_user import CreateUserUseCase
from api.infrastructure.db.sql.session_sqlite import get_session
from api.infrastructure.repositories.sql.user_repository import SQLUserRepository
from api.interface.controllers.user_controller import UserController

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/user/create")
def create_user(name: str, session: Session = Depends(get_session)):
    repo = SQLUserRepository(session)
    use_case = CreateUserUseCase(repo)
    controller = UserController(use_case)
    return controller.create(name)
