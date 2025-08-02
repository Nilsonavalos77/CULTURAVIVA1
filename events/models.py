from django.db import models

class Event(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True) # <-- Añade esta línea