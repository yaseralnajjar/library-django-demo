from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Book

User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'books_count')


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'isbn', 'publish_date', 'author')
