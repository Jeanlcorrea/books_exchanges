from django.urls import path

from books.views.insert_books_api_view import InsertBooksAPIView
from books.views.list_all_available_books_api_view import ListAllAvailableBooks

app_name = 'books'

urlpatterns = [
    path(f'{app_name}/insert', InsertBooksAPIView.as_view()),
    path(f'{app_name}/list', ListAllAvailableBooks.as_view())
]
