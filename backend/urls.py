from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),     # ahora todo lo de usuarios va por /api/users/
    path('api/eventos/', include('events.urls')),  # y eventos por /api/eventos/
    path('api/login/', obtain_auth_token),         # login por token
]
