from django.urls import path

from notifications.views.list_all_unread_notifications_by_username_api_view import ListAllUnreadNotificationsByUsername

app_name = 'notifications'

urlpatterns = [
    path(f'{app_name}/<str:username>', ListAllUnreadNotificationsByUsername.as_view()),
]
