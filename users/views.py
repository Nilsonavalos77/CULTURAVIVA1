# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny # Importante para que no necesiten autenticarse para iniciar sesión

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny] # Permite el acceso sin autenticación previa

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Opcional: Si usas sesiones de Django junto con DRF
            # Esto establecerá la cookie de sesión de Django
            login(request, user)
            return Response({"message": "Login successful", "user_id": user.id}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

