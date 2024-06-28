from books.factories import BooksFactories
from exchanges.contracts.repositories import IExchangesRepository
from exchanges.repositories.database import ExchangePostgres
from exchanges.services.request_exchange_use_case import RequestExchangeUseCase
from users.factories import UserFactories


class ExchangesFactories:

    @staticmethod
    def make_exchanges_repository() -> IExchangesRepository:
        return ExchangePostgres()

    @classmethod
    def make_request_exchange_use_case(cls) -> RequestExchangeUseCase:
        return RequestExchangeUseCase(
            users_repository=UserFactories.make_users_repository(),
            books_repository=BooksFactories.make_books_repository(),
            exchanges_repository=cls.make_exchanges_repository()
        )
