from enum import Enum, EnumMeta
from typing import List


class BooksExchangeEnum(Enum):

    @classmethod
    def choices(cls, **kwargs):
        return choices_from_enum(cls, **kwargs)


def choices_from_enum(enum_: EnumMeta, field_pattern: tuple = ("value", "value")) -> List[tuple]:
    first_field, second_field = field_pattern
    return [(getattr(choice, first_field), getattr(choice, second_field)) for choice in enum_]
