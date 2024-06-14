from rest_framework import status
from rest_framework.request import Request as RestFrameworkRequest
from drf_yasg.utils import swagger_auto_schema

from books.factories import BooksFactories
from books.filter import ListBooksFilter
from books.serializers import ListBooksQuerySerializer, ListBooksOutputSerializer
from utils.custom_api_view import BooksExchangeAPIView
from utils.pagination import Pagination


class ListAllAvailableBooks(BooksExchangeAPIView):

    def __init__(self):
        super().__init__()
        self._books_repository = BooksFactories.make_books_repository()
        self._pagination = Pagination()

    @swagger_auto_schema(
        query_serializer=ListBooksQuerySerializer(),
        responses={status.HTTP_200_OK: ListBooksOutputSerializer()}
    )
    def get(self, request: RestFrameworkRequest):
        serializer = ListBooksQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        all_books = self._books_repository.list_all()

        filtered = ListBooksFilter(data=serializer.validated_data, queryset=all_books)

        page = self._pagination.paginate_queryset(queryset=filtered.qs, request=request)

        output = ListBooksOutputSerializer(page, many=True)

        return self._pagination.get_paginated_response(data=output.data)
