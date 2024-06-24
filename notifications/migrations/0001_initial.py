# Generated by Django 5.0.6 on 2024-06-24 22:21

import django.db.models.deletion
import django_extensions.db.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModels',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('message', models.CharField(db_column='MESSAGE', max_length=500)),
                ('is_read', models.BooleanField(db_column='IS_READ', default=False)),
                ('user', models.ForeignKey(db_column='USER', on_delete=django.db.models.deletion.CASCADE, to='users.usermodels')),
            ],
            options={
                'verbose_name': 'NOTIFICATION',
                'verbose_name_plural': 'NOTIFICATIONS',
                'db_table': 'NOTIFICATIONS',
            },
        ),
    ]
