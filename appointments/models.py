from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    timezone = models.CharField(max_length=50)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meeting scheduled by {self.name} on {self.meeting_date} at {self.meeting_time}"