import uuid

from django.db import models


class UserModels(models.Model):
    id = models.UUIDField(db_column='ID', primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(db_column='USERNAME', max_length=200)
    password = models.CharField(db_column='PASSWORD', max_length=200)
    email = models.CharField(db_column='EMAIL', unique=True)
    address = models.JSONField(db_column='ADDRESS')
    is_active = models.BooleanField(db_column='IS_ACTIVE', default=True)
    is_staff = models.BooleanField(db_column='IS_STAFF', default=False)

    class Meta:
        db_table = 'USERS'
        verbose_name = 'USER'
        verbose_name_plural = 'USERS'
