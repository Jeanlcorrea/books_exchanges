from books.models import BookModels
from exchanges.contracts.repositories import IExchangesRepository
from exchanges.enums import BookExchangeStatus
from exchanges.models import ExchangeModels
from users.models import UserModels


class ExchangePostgres(IExchangesRepository):

    def create_exchange(self,
                        book: BookModels,
                        requester: UserModels,
                        owner: UserModels,
                        status: BookExchangeStatus) -> ExchangeModels:
        return self.model.objects.create(book=book,
                                         requester=requester,
                                         owner=owner,
                                         status=status)
