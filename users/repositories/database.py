from users.contracts.repositories import IUsersRepository
from users.entity import UserEntity
from users.types import UserAddress


class UsersPostgres(IUsersRepository):

    def find_user_by_username(self, username: str):
        return self.safe_get(username=username)

    def create_user(self,
                    username: str,
                    password: str,
                    email: str,
                    address: UserAddress) -> UserEntity:
        return self.model.objects.create(username=username,
                                         password=password,
                                         email=email,
                                         address=address)
