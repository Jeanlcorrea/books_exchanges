from rest_framework import status
from rest_framework.response import Response
from users.factories import UserFactories
from users.serializers import UserInputSerializer, UserOutputSerializer
from utils.custom_api_view import BooksExchangeAPIView
from rest_framework.request import Request as RestFrameworkRequest
from drf_yasg.utils import swagger_auto_schema


class CreateUserAPIView(BooksExchangeAPIView):

    def __init__(self):
        super().__init__()
        self._create_user_use_case = UserFactories.make_create_user_use_case()

    @swagger_auto_schema(
        request_body=UserInputSerializer(),
        responses={status.HTTP_201_CREATED: UserOutputSerializer()}
    )
    def post(self, request: RestFrameworkRequest):
        serializer = UserInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self._create_user_use_case.execute(
            username=serializer.validated_data.get('username'),
            password=serializer.validated_data.get('password'),
            email=serializer.validated_data.get('email'),
            address=serializer.validated_data.get('address')
        )

        output = UserOutputSerializer(instance=user)

        return Response(data=output.data, status=status.HTTP_201_CREATED)
