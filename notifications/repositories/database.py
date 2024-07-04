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

    def find_all_unread_notifications_by_user(self, user: str):
        return self.model.objects.filter(is_read=False, user=user)
