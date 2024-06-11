from abc import abstractmethod
from datetime import date

from books.models import BookModels
from users.entity import UserEntity
from utils.contracts import IRepository


class IBooksRepository(IRepository):
    model = BookModels

    @abstractmethod
    def insert_book(self,
                    title: str,
                    author: str,
                    published_date: date,
                    genre: str,
                    owner: UserEntity):
        return NotImplemented()
