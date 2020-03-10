from django.urls import path

from .views import AuthorListAPIView, BookDetailAPIView, BookListCreateAPIView

app_name = 'core'

books_urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='detail'),
]

authors_urlpatterns = [
    path('', AuthorListAPIView.as_view(), name='list'),
]
