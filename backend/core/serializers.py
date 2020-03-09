from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'isbn', 'publish_date', 'author')
