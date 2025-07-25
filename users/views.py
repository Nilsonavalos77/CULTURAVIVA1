from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token  # <-- Necesario para tokens
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserLoginAPIView(APIView):
    """
    Vista para el inicio de sesión de usuarios.
    Permite a cualquier usuario (no autenticado) iniciar sesión.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generar o recuperar el token para el usuario
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "message": "Login successful",
                "user_id": user.id,
                "token": token.key
            }, status=status.HTTP_200_OK)

        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]