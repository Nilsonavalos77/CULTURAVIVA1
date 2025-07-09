from rest_framework import viewsets
from .models import Evento
from .serializers import EventoSerializer, UserSerializer
from django.contrib.auth.models import User

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
