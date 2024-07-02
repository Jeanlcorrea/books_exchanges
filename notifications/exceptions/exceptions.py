from utils.exceptions import ObjectNotFound


class ThereIsNotNotifications(ObjectNotFound):
    DEFAULT_MESSAGE = 'There is not notification for this user.'
    DEFAULT_CODE = 'THERE_IS_NOT_NOTIFICATIONS'
    DEFAULT_STATUS_CODE = 400

    def __init__(self, message: str = DEFAULT_MESSAGE, code: str = DEFAULT_CODE,
                 status_code: int = DEFAULT_STATUS_CODE):
        super().__init__(message=message, code=code, status_code=status_code)
