from rest_framework import serializers

from books.enums import GenreChoices


class InsertBooksUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, help_text='username')
    email = serializers.CharField(max_length=254, help_text='user@email.com')


class InsertBooksInputDataSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    published_date = serializers.IntegerField()
    genre = serializers.ChoiceField(choices=GenreChoices.choices())
    owner = serializers.CharField(max_length=200, help_text='your_username')


class InsertBooksOutputDataSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    published_date = serializers.IntegerField()
    genre = serializers.CharField(max_length=30)
    is_available_for_exchange = serializers.BooleanField()
    owner = InsertBooksUserSerializer()


class ListBooksQuerySerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    author = serializers.CharField(required=False)
    published_date = serializers.IntegerField(required=False, help_text='YEAR')
    genre = serializers.ChoiceField(required=False, choices=GenreChoices.choices())
    is_available_for_exchange = serializers.BooleanField(required=False, help_text='[TRUE, FALSE]', default=True)
    limit = serializers.IntegerField(required=False, default=10)
    offset = serializers.IntegerField(required=False, default=0)
    ordering = serializers.ChoiceField(
        required=False,
        default='-published_date',
        choices=[
            'id', '-id',
            'title', '-title',
            'author', '-author',
            'published_date', '-published_date',
            'genre', '-genre',
            'is_available_for_exchange', '-is_available_for_exchange'
        ]
    )


class ListBooksOutputSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    published_date = serializers.IntegerField()
    genre = serializers.CharField(max_length=30)
    is_available_for_exchange = serializers.BooleanField()
