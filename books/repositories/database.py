from datetime import date
from typing import Union
from uuid import UUID

from books.contracts.repositories import IBooksRepository
from users.entity import UserEntity


class BooksPostgres(IBooksRepository):

    def insert_book(self,
                    title: str,
                    author: str,
                    published_date: date,
                    genre: str,
                    owner: UserEntity):
        return self.model.objects.create(title=title,
                                         author=author,
                                         published_date=published_date,
                                         genre=genre,
                                         is_available_for_exchange=True,
                                         owner=owner)

    def list_all(self):
        return self.model.objects.all()

    def find_book_by_id(self, book_id: Union[UUID, str]):
        return self.safe_get(id=book_id)
