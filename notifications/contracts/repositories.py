from abc import abstractmethod

from notifications.models import NotificationModels
from users.models import UserModels
from utils.contracts import IRepository


class INotificationsRepository(IRepository):
    model = NotificationModels

    @abstractmethod
    def create_notification(self,
                            user: UserModels,
                            message: str,
                            is_read: bool = False):
        return NotImplementedError()
