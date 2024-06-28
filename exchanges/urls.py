from django.urls import path

from exchanges.views.request_exchange_api_view import RequestExchangeAPIView

app_name = 'exchanges'

urlpatterns = [
    path(f'{app_name}/<str:username>/<str:book_id>', RequestExchangeAPIView.as_view()),
]
