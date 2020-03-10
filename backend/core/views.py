from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db.models.functions import Coalesce
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .permissions import IsBookAuthor
from .serializers import AuthorSerializer, BookSerializer

User = get_user_model()


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'first_name', 'books_count']

    def get_queryset(self):
        '''
        we use Coalesce to make sure no nulls returned from summation of books
        https://stackoverflow.com/a/35413920/4565520
        '''
        return User.objects.annotate(books_count=Coalesce(Count('book'), 0))\
                           .values('id', 'first_name', 'books_count')


class BookListCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'name', 'isbn', 'publish_date', 'author']

    def get_queryset(self):
        return Book.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated, IsBookAuthor)
