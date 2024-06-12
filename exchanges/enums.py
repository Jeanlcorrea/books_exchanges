from utils.enums import BooksExchangeEnum


class BookExchangeStatus(BooksExchangeEnum):
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
