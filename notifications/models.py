import uuid
from django.db import models
from django_extensions.db.models import TimeStampedModel
from users.models import UserModels


class NotificationModels(TimeStampedModel):
    id = models.UUIDField(db_column='ID', primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(UserModels, db_column='USER', on_delete=models.CASCADE)
    message = models.CharField(db_column='MESSAGE', max_length=500)
    is_read = models.BooleanField(db_column='IS_READ', default=False)

    class Meta:
        db_table = 'NOTIFICATIONS'
        verbose_name = 'NOTIFICATION'
        verbose_name_plural = 'NOTIFICATIONS'
