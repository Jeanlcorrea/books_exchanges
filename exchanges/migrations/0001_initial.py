# Generated by Django 5.0.6 on 2024-06-12 18:17

import django.db.models.deletion
import django_extensions.db.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeModels',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED')], db_column='STATUS', max_length=30)),
                ('book', models.ForeignKey(db_column='BOOK', on_delete=django.db.models.deletion.CASCADE, to='books.bookmodels')),
                ('owner', models.ForeignKey(db_column='OWNER', on_delete=django.db.models.deletion.CASCADE, related_name='owner_exchanges', to='users.usermodels')),
                ('requester', models.ForeignKey(db_column='REQUESTER', on_delete=django.db.models.deletion.CASCADE, related_name='requested_exchanges', to='users.usermodels')),
            ],
            options={
                'verbose_name': 'EXCHANGE',
                'verbose_name_plural': 'EXCHANGES',
                'db_table': 'EXCHANGES',
            },
        ),
    ]
