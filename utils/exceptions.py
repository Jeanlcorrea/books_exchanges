from rest_framework import status
from rest_framework.exceptions import ValidationError


class BooksExchangeValidationError(ValidationError):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, message=None, code=None, status_code: int = status_code):
        if status_code != self.status_code:
            self.status_code = status_code

        self.error_message = message
        self.code = code

        super().__init__(detail=message, **{"code": code} if code else {})

class ObjectNotFound(BooksExchangeValidationError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
