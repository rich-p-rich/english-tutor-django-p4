from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta

MAX_APPOINTMENT_WEEKS = 4
MIN_APPOINTMENT_DAYS = 1  # New constant for minimum appointment days

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

    def clean(self):
        # Ensure meeting date is within the valid range
        today = timezone.now().date()
        min_date = today + timedelta(days=MIN_APPOINTMENT_DAYS)
        max_date = today + timedelta(weeks=MAX_APPOINTMENT_WEEKS)

        if self.meeting_date is None:
            raise ValidationError("Please check the appointment date.")
        
        if not (min_date <= self.meeting_date <= max_date):
            raise ValidationError(f"Meeting date must be between {min_date} and {max_date}.")