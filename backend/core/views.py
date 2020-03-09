from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .permissions import IsBookAuthor
from .serializers import BookSerializer


class BookListCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Book.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated, IsBookAuthor)
