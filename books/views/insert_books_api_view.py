from rest_framework import status
from rest_framework.response import Response

from books.factories import BooksFactories
from books.serializers import InsertBooksInputDataSerializer, InsertBooksOutputDataSerializer
from utils.custom_api_view import BooksExchangeAPIView
from rest_framework.request import Request as RestFrameworkRequest
from drf_yasg.utils import swagger_auto_schema


class InsertBooksAPIView(BooksExchangeAPIView):

    def __init__(self):
        super().__init__()
        self._insert_books_use_case = BooksFactories.make_insert_books_user_case()

    @swagger_auto_schema(
        request_body=InsertBooksInputDataSerializer(),
        responses={status.HTTP_201_CREATED: InsertBooksOutputDataSerializer()}
    )
    def post(self, request: RestFrameworkRequest):
        serializer = InsertBooksInputDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        book = self._insert_books_use_case.execute(title=serializer.validated_data.get('title'),
                                                   author=serializer.validated_data.get('author'),
                                                   genre=serializer.validated_data.get('genre'),
                                                   owner=serializer.validated_data.get('owner'),
                                                   published_date=serializer.validated_data.get('published_date'))

        output = InsertBooksOutputDataSerializer(instance=book)

        return Response(data=output.data, status=status.HTTP_201_CREATED)
