from api.application.use_cases.create_user import CreateUserUseCase


class UserController:
    def __init__(self, use_case: CreateUserUseCase):
        self.use_case = use_case

    def create(self, name: str):
        return self.use_case.execute(name)
