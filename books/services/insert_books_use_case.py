from datetime import date

from books.contracts.repositories import IBooksRepository
from books.exception.exceptions import UserDoesNotExists
from notifications.contracts.repositories import INotificationsRepository
from users.contracts.repositories import IUsersRepository


class InsertBooksUseCase:

    def __init__(self, users_repository: IUsersRepository,
                 books_repository: IBooksRepository,
                 notifications_repository: INotificationsRepository):
        self._users_repository = users_repository
        self._books_repository = books_repository
        self._notifications_repository = notifications_repository

    def execute(self,
                title: str,
                author: str,
                published_date: date,
                genre: str,
                owner: str):
        user = self._users_repository.find_user_by_username(username=owner)

        if not user:
            raise UserDoesNotExists()

        insert_book = self._books_repository.insert_book(title=title,
                                                         author=author,
                                                         published_date=published_date,
                                                         genre=genre,
                                                         owner=user)

        self._notifications_repository.create_notification(
            user=user,
            message=f'Your book | id: {insert_book.id} title: {insert_book.title} | has been added'
        )

        return insert_book
