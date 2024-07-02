from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request as RestFrameworkRequest
from drf_yasg.utils import swagger_auto_schema

from notifications.exceptions.exceptions import ThereIsNotNotifications
from notifications.factories import NotificationsFactories
from notifications.serializers import NotificationsOutputSerializer
from users.factories import UserFactories
from utils.custom_api_view import BooksExchangeAPIView
from utils.pagination import Pagination


class ListAllUnreadNotificationsByUsername(BooksExchangeAPIView):

    def __init__(self):
        super().__init__()
        self._notifications_repository = NotificationsFactories.make_notifications_repository()
        self._user_repository = UserFactories.make_users_repository()
        self._pagination = Pagination()

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: NotificationsOutputSerializer()}
    )
    def get(self, request: RestFrameworkRequest, username: str):
        user = self._user_repository.find_user_by_username(username=username)
        all_notifications = self._notifications_repository.find_all_unread_notifications_by_user(user=user)

        for notification in all_notifications:
            notification.is_read = True
            notification.save()

        page = self._pagination.paginate_queryset(queryset=all_notifications, request=request)

        output = NotificationsOutputSerializer(instance=page, many=True)

        return Response(data=output.data, status=status.HTTP_200_OK)
