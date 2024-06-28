from books.contracts.repositories import IBooksRepository
from exchanges.contracts.repositories import IExchangesRepository
from exchanges.enums import BookExchangeStatus
from exchanges.exceptions.exceptions import UserOrBookDoesNotExists
from users.contracts.repositories import IUsersRepository


class RequestExchangeUseCase:

    def __init__(self, users_repository: IUsersRepository,
                 books_repository: IBooksRepository,
                 exchanges_repository: IExchangesRepository):
        self._users_repository = users_repository
        self._books_repository = books_repository
        self._exchanges_repository = exchanges_repository

    def execute(self, username, book_id):
        requester = self._users_repository.find_user_by_username(username=username)
        book = self._books_repository.find_book_by_id(book_id=book_id)

        if not requester and book:
            raise UserOrBookDoesNotExists()

        request_exchange =  self._exchanges_repository.create_exchange(book=book,
                                                                       requester=requester,
                                                                       owner=book.owner,
                                                                       status=BookExchangeStatus.PENDING.value)

        return request_exchange
