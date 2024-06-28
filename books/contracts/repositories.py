from abc import abstractmethod
from datetime import date
from typing import Union
from uuid import UUID

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
        return NotImplementedError()

    @abstractmethod
    def list_all(self):
        return NotImplementedError()

    @abstractmethod
    def find_book_by_id(self, book_id: Union[UUID, str]):
        return NotImplementedError()
