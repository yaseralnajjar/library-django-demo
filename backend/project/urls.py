from django.contrib import admin
from django.urls import path, include

from core import views
from accounts.views import UserRegistrationAPIView, UserLoginAPIView, UserTokenAPIView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/users/', UserRegistrationAPIView.as_view(), name="list"),
    path('api/auth/users/login/', UserLoginAPIView.as_view(), name="login"),
    path('api/auth/tokens/<key>/', UserTokenAPIView.as_view(), name="token"),
    
    path('api/hello/', views.HelloView.as_view(), name='hello'),
]
