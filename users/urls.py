
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token # Si quieres usar la vista de token de DRF
from .views import UserCreateAPIView, UserLoginAPIView # ¡Importa AMBAS vistas!

urlpatterns = [
    # Ruta para el registro de usuarios
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    
    # Ruta para el inicio de sesión con tu vista personalizada
    path('login/', UserLoginAPIView.as_view(), name='user-login'),

    #Ruta para el inicio de sesión que devuelve un token (si lo usas en el frontend)
     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]