from django.urls import path

from .views import BookDetailAPIView, BookListCreateAPIView

app_name = 'core'

urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name="list"),
    path('<int:pk>/', BookDetailAPIView.as_view(), name="detail"),
]
