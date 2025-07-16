from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer

# Lista y creación de eventos
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Obtener, actualizar y eliminar un evento específico
class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo permite acceso a eventos del usuario autenticado
        return self.queryset.filter(user=self.request.user)

