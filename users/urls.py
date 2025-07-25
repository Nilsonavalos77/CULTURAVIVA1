from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserLoginAPIView 

urlpatterns = [
 # path('register/', UserCreateAPIView.as_view(), name='user-register'), # Línea comentada o eliminada
 path('api/users/login/', obtain_auth_token), # DRF built-in token login
 path('login/', UserLoginAPIView.as_view(), name='user-login'), # Tu custom login
]