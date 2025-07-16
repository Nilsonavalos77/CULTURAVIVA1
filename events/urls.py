# events/urls.py

from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDestroyView

urlpatterns = [
    path('', EventListCreateView.as_view(), name='event-list-create'),              # /api/eventos/
    path('<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-detail')  # /api/eventos/1/
]
