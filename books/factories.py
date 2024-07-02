from books.contracts.repositories import IBooksRepository
from books.repositories.database import BooksPostgres
from books.services.insert_books_use_case import InsertBooksUseCase
from notifications.factories import NotificationsFactories
from users.factories import UserFactories


class BooksFactories:

    @staticmethod
    def make_books_repository() -> IBooksRepository:
        return BooksPostgres()

    @classmethod
    def make_insert_books_user_case(cls) -> InsertBooksUseCase:
        return InsertBooksUseCase(
            users_repository=UserFactories.make_users_repository(),
            books_repository=cls.make_books_repository(),
            notifications_repository=NotificationsFactories.make_notifications_repository()
        )
