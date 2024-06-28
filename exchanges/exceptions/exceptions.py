from utils.exceptions import ObjectNotFound


class UserOrBookDoesNotExists(ObjectNotFound):
    DEFAULT_MESSAGE = 'This user or book does not exists. Please, try again.'
    DEFAULT_CODE = 'USER_DOES_NOT_EXISTS'
    DEFAULT_STATUS_CODE = 400

    def __init__(self, message: str = DEFAULT_MESSAGE, code: str = DEFAULT_CODE,
                 status_code: int = DEFAULT_STATUS_CODE):
        super().__init__(message=message, code=code, status_code=status_code)
