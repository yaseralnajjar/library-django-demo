
from core.urls import authors_urlpatterns, books_urlpatterns
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('accounts.urls')),
    path('api/books/', include((books_urlpatterns, 'core'), namespace='books')),
    path('api/authors/', include((authors_urlpatterns, 'core'), namespace='authors')),
]
