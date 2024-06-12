import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel

from books.models import BookModels
from exchanges.enums import BookExchangeStatus
from users.models import UserModels


class ExchangeModels(TimeStampedModel):
    id = models.UUIDField(db_column='ID', primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(BookModels, db_column='BOOK', on_delete=models.CASCADE)
    requester = models.ForeignKey(UserModels, db_column='REQUESTER',
                                  on_delete=models.CASCADE, related_name='requested_exchanges')
    owner = models.ForeignKey(UserModels, db_column='OWNER',
                              on_delete=models.CASCADE, related_name='owner_exchanges')
    status = models.CharField(db_column='STATUS', max_length=30, choices=BookExchangeStatus.choices())

    class Meta:
        db_table = 'EXCHANGES'
        verbose_name = 'EXCHANGE'
        verbose_name_plural = 'EXCHANGES'
