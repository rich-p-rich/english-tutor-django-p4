from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    name = models.CharField(max_length=100, default='name')
    surname = models.CharField(max_length=100, default='surname')
    email = models.EmailField(max_length=255, default='email')
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    message = models.TextField(max_length=1000, default='message')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meeting scheduled by {self.name} on {self.meeting_date} at {self.meeting_time}"