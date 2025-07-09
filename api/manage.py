from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
