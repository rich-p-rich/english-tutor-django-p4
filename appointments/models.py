from django.db import models
from django.contrib.auth.models import User
from user_accounts.models import UserProfile
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta, time

# Define max / min time range 
MAX_APPOINTMENT_WEEKS = 4 # Appt can be max 4 weeks in the future
MIN_APPOINTMENT_DAYS = 1  # Appt must be min 1 day in the future

# Define time range constants
MORNING_START_TIME = time(8, 0)  # 08:00
MORNING_END_TIME = time(12, 30)  # 12:30
AFTERNOON_START_TIME = time(14, 0)  # 14:00
AFTERNOON_END_TIME = time(18, 0)  # 18:00

class Appointment(models.Model):
    # User profile comes from the app 'user_accounts' -> model
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    message = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meeting scheduled by {self.name} on {self.meeting_date} at {self.meeting_time}"

    def clean(self):
        # Ensures the meeting date is within the valid range
        today = timezone.now().date()
        min_date = today + timedelta(days=MIN_APPOINTMENT_DAYS)
        max_date = today + timedelta(weeks=MAX_APPOINTMENT_WEEKS)

        if self.meeting_date is None:
            raise ValidationError("Please check your appointment date:")
        
        if not (min_date <= self.meeting_date <= max_date):
            raise ValidationError(f"Meeting date must be between {min_date} and {max_date}.")

        # Ensures the meeting time is within the allowed ranges
        if not (MORNING_START_TIME <= self.meeting_time <= MORNING_END_TIME or
                AFTERNOON_START_TIME <= self.meeting_time <= AFTERNOON_END_TIME):
            raise ValidationError(f"Please choose a different time. Our appointments run between {MORNING_START_TIME.strftime('%H:%M')} and {MORNING_END_TIME.strftime('%H:%M')}, and between {AFTERNOON_START_TIME.strftime('%H:%M')} and {AFTERNOON_END_TIME.strftime('%H:%M')}.")

def save(self, *args, **kwargs):
    # Calls the full_clean method to ensure form validations are run before saving
    self.full_clean()
    super(Appointment, self).save(*args, **kwargs)
