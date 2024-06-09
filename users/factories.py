from users.contracts.repositories import IUsersRepository
from users.repositories.database import UsersPostgres
from users.services.create_user_use_case import CreateUserUseCase


class UserFactories:

    @staticmethod
    def make_users_repository() -> IUsersRepository:
        return UsersPostgres()

    @classmethod
    def make_create_user_use_case(cls) -> CreateUserUseCase:
        return CreateUserUseCase(
            users_repository=cls.make_users_repository()
        )
