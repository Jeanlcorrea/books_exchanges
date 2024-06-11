from rest_framework import serializers

from books.enums import GenreChoices


class InsertBooksUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, help_text='username')
    email = serializers.CharField(max_length=254, help_text='user@email.com')


class InsertBooksInputDataSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField()
    genre = serializers.ChoiceField(choices=GenreChoices.choices())
    owner = serializers.CharField(max_length=200, help_text='your_username')


class InsertBooksOutputDataSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField()
    genre = serializers.CharField(max_length=30)
    is_available_for_exchange = serializers.BooleanField()
    owner = InsertBooksUserSerializer()
