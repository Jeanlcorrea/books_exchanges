from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request as RestFrameworkRequest
from drf_yasg.utils import swagger_auto_schema

from exchanges.enums import BookExchangeStatus
from exchanges.types import RequestExchangeReturnDict
from utils.custom_api_view import BooksExchangeAPIView


class RequestExchangeAPIView(BooksExchangeAPIView):

    def __init__(self):
        super().__init__()

    @swagger_auto_schema(
        responses={status.HTTP_202_ACCEPTED: ''}
    )
    def post(self, request: RestFrameworkRequest, requester, book_id):
        my_service = ''

        output = RequestExchangeReturnDict(
            message="Your book exchange request has been received and is pending evaluation.",
            status=BookExchangeStatus.PENDING.value
        )

        return Response(data=output, status=status.HTTP_202_ACCEPTED)
