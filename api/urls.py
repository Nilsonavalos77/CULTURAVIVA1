from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, UserViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'usuarios', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
