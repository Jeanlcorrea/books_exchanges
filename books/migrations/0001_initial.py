# Generated by Django 5.0.6 on 2024-06-24 22:21

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookModels',
            fields=[
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(db_column='TITLE', max_length=200)),
                ('author', models.CharField(db_column='AUTHOR', max_length=100)),
                ('published_date', models.IntegerField(db_column='PUBLISH_DATE')),
                ('genre', models.CharField(choices=[('FICTION', 'FICTION'), ('NON_FICTION', 'NON_FICTION'), ('MISTERY', 'MISTERY'), ('FANTASY', 'FANTASY'), ('BIOGRAPHY', 'BIOGRAPHY'), ('SCIENCE_FICTION', 'SCIENCE_FICTION'), ('ROMANCE', 'ROMANCE'), ('HORROR', 'HORROR'), ('HISTORY', 'HISTORY'), ('CHILDREN', 'CHILDREN')], db_column='GENRE', max_length=30)),
                ('is_available_for_exchange', models.BooleanField(db_column='IS_AVAILABLE_FOR_EXCHANGE')),
                ('owner', models.ForeignKey(db_column='OWNER', on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to='users.usermodels')),
            ],
            options={
                'verbose_name': 'BOOK',
                'verbose_name_plural': 'BOOKS',
                'db_table': 'BOOKS',
            },
        ),
    ]
