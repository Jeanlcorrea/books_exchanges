from notifications.contracts.repositories import INotificationsRepository
from users.models import UserModels


class NotificationPostgres(INotificationsRepository):

    def create_notification(self,
                            user: UserModels,
                            message: str,
                            is_read: bool = False):
        return self.model.objects.create(user=user,
                                         message=message,
                                         is_read=is_read)
