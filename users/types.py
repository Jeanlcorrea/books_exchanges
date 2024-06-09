from typing import Type


class UserAddress(Type):
    cep: str
    state: str
    city: str
