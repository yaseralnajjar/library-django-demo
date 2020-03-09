
from core import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('accounts.urls')),

    path('api/hello/', views.HelloView.as_view(), name='hello'),
]
