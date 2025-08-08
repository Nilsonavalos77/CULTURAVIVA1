from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Una vista simple para confirmar que el servidor está funcionando
    path('', lambda request: HttpResponse("¡Servidor Django funcionando! Accede a /admin/, /api/users/ o /api/eventos/"), name='home-api'),
    
    # Rutas para el panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Rutas de la API para los usuarios y los eventos
    path('api/users/', include('users.urls')),
    path('api/eventos/', include('events.urls')),
    
    # Endpoint para la autenticación de usuarios y obtención de tokens
    path('api/users/login/', obtain_auth_token),
]

# Esta condición es crucial para servir archivos de media (imágenes) en modo de desarrollo.
# Se asegura de que las URLs de media sean accesibles.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



