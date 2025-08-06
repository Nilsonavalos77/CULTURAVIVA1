from django.db import models

class Event(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()  # sin tilde
    ubicacion = models.CharField(max_length=255)  # sin tilde
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True)
    # Campo para registrar cuándo se creó el evento
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']  # Mostrará primero los eventos más recientes
