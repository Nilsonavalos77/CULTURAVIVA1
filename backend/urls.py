from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', lambda request: HttpResponse("¡Servidor Django funcionando! Accede a /admin/, /api/users/ o /api/eventos/"), name='home-api'),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # <-- ¡Aquí está la clave!
    path('api/eventos/', include('events.urls')),
    path('api/users/login/', obtain_auth_token),
]


