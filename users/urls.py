from django.urls import path

from users.views.create_user_api_view import CreateUserAPIView

app_name = 'users'

urlpatterns = [
    path(f'{app_name}/create', CreateUserAPIView.as_view())
]
