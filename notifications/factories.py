from notifications.contracts.repositories import INotificationsRepository
from notifications.repositories.database import NotificationPostgres


class NotificationsFactories:

    @staticmethod
    def make_notifications_repository() -> INotificationsRepository:
        return NotificationPostgres()
