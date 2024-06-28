from abc import abstractmethod

from books.models import BookModels
from exchanges.enums import BookExchangeStatus
from exchanges.models import ExchangeModels
from users.models import UserModels
from utils.contracts import IRepository


class IExchangesRepository(IRepository):
    model = ExchangeModels

    @abstractmethod
    def create_exchange(self,
                        book: BookModels,
                        requester: UserModels,
                        owner: UserModels,
                        status: BookExchangeStatus):
        return NotImplementedError()
