from django.db import models
from django.contrib.auth.models import User 
class Event(models.Model):
    """
    Modelo para representar un evento.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True) 
    date_time = models.DateTimeField() 
    location = models.CharField(max_length=255)
    capacity = models.IntegerField(default=0) 
    is_active = models.BooleanField(default=True) 
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title

class Registration(models.Model):
    """
    Modelo para representar la inscripción de un usuario a un evento.
    Esta es nuestra tabla intermedia para la relación Many-to-Many entre User y Event.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations') 
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations') 
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='registered') 

    class Meta:
        unique_together = ('user', 'event') 
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"