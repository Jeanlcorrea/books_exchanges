from notifications.contracts.repositories import INotificationsRepository
from users.contracts.repositories import IUsersRepository
from users.entity import UserEntity
from users.types import UserAddress


class CreateUserUseCase:

    def __init__(self,
                 users_repository: IUsersRepository,
                 notifications_repository: INotificationsRepository):
        self._users_repository = users_repository
        self._notifications_repository = notifications_repository

    def execute(self,
                username: str,
                password: str,
                email: str,
                address: UserAddress) -> UserEntity:
        user = self._users_repository.find_user_by_username(username=username)

        if not user:
            user = self._users_repository.create_user(username=username,
                                                      password=password,
                                                      email=email,
                                                      address=address)

        self._notifications_repository.create_notification(
            user=user,
            message=f'Welcome to Book Exchange APIs  {user.username}!'
        )

        return user
