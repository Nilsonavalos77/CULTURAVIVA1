# events/views.py
from rest_framework import generics
from rest_framework import permissions # <--- ¡Importa permissions!
from .models import Event
from .serializers import EventSerializer

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # Para que cualquiera pueda ver (GET), pero solo autenticados puedan crear (POST)
    permission_classes = [permissions.AllowAny]