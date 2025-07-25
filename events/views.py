from rest_framework import generics
from .models import Event  # Asegurate que el modelo exista
from .serializers import EventSerializer  # Asegurate que esté creado

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
