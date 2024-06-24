import uuid

from django.db import models

from books.enums import GenreChoices
from users.models import UserModels


class BookModels(models.Model):
    id = models.UUIDField(db_column='ID', primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(db_column='TITLE', max_length=200)
    author = models.CharField(db_column='AUTHOR', max_length=100)
    published_date = models.IntegerField(db_column='PUBLISH_DATE')
    genre = models.CharField(db_column='GENRE', max_length=30, choices=GenreChoices.choices())
    is_available_for_exchange = models.BooleanField(db_column='IS_AVAILABLE_FOR_EXCHANGE')
    owner = models.ForeignKey(UserModels, on_delete=models.DO_NOTHING, db_column='OWNER', related_name='owner')

    class Meta:
        db_table = 'BOOKS'
        verbose_name = 'BOOK'
        verbose_name_plural = 'BOOKS'
