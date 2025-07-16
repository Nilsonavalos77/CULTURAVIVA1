from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer

# Lista y creación de eventos
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]  # ✅ acceso libre temporal

# Obtener, actualizar y eliminar un evento específico
class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]  # ✅ acceso libre temporal

    def get_queryset(self):
        return self.queryset.all()  # ✅ sin filtrar por usuario

