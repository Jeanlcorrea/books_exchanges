from abc import abstractmethod

from users.entity import UserEntity
from users.models import UserModels
from users.types import UserAddress
from utils.contracts import IRepository


class IUsersRepository(IRepository):
    model = UserModels

    @abstractmethod
    def find_user_by_username(self, username: str):
        raise NotImplemented()

    @abstractmethod
    def create_user(self,
                    username: str,
                    password: str,
                    email: str,
                    address: UserAddress) -> UserEntity:
        raise NotImplemented()
