from datetime import date

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
