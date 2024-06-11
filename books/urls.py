from django.urls import path

from books.views.insert_books_api_view import InsertBooksAPIView

app_name = 'books'

urlpatterns = [
    path(f'{app_name}/insert', InsertBooksAPIView.as_view())
]
