# C:\Users\bnoel\Documents\haiuhiq\CULTURAVIVA1\users\serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User # Importa el modelo User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password') # Define los campos que se pueden serializar
        extra_kwargs = {'password': {'write_only': True}} # Hace que la contraseña sea de solo escritura (no se muestra al obtener el usuario)

    def create(self, validated_data):
        # Sobrescribe el método create para manejar el hash de la contraseña
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''), # El email puede ser opcional
            password=validated_data['password']
        )
        return user