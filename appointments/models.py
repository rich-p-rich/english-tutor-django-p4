from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta, time
from django.contrib.auth.models import User
from user_accounts.models import UserProfile
from django.db.models import Q

# Define max / min time range
MAX_APPOINTMENT_WEEKS = 4  # Appt can be max 4 weeks in the future
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
    message = models.TextField(max_length=1000, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Meeting scheduled by {self.user_profile.name} on "
            f"{self.meeting_date} at {self.meeting_time}"
        )

    def clean(self):
        # Ensures the meeting date is within the valid range
        today = timezone.now().date()
        min_date = today + timedelta(days=MIN_APPOINTMENT_DAYS)
        max_date = today + timedelta(weeks=MAX_APPOINTMENT_WEEKS)
        # Sets meeting duration of 30mns with a 10min buffer
        meeting_duration = timedelta(minutes=40)

        if self.meeting_date is None:
            raise ValidationError("Please check your appointment date:")

        if not (min_date <= self.meeting_date <= max_date):
            raise ValidationError(
                f"Your appointment must be between {min_date} and {max_date}."
            )

        # Ensures the meeting time is within the allowed ranges
        if not (
            MORNING_START_TIME <= self.meeting_time <= MORNING_END_TIME or
            AFTERNOON_START_TIME <= self.meeting_time <= AFTERNOON_END_TIME
        ):
            raise ValidationError(
                f"Please choose a different time. Our appointments run "
                f"between {MORNING_START_TIME.strftime('%H:%M')} and "
                f"{MORNING_END_TIME.strftime('%H:%M')}, and between "
                f"{AFTERNOON_START_TIME.strftime('%H:%M')} and "
                f"{AFTERNOON_END_TIME.strftime('%H:%M')}."
            )

        # Calculate the start and end times for the appointment
        meeting_start = datetime.combine(self.meeting_date, self.meeting_time)
        meeting_end = meeting_start + meeting_duration

        # Check for overlapping appointments
        overlapping_appointments = Appointment.objects.filter(
            Q(meeting_date=self.meeting_date) & (
                Q(meeting_time__gte=self.meeting_time,
                  meeting_time__lt=meeting_end.time()) |
                Q(meeting_time__lt=self.meeting_time,
                  meeting_time__gte=(meeting_start - meeting_duration).time())
            )
        )

        if overlapping_appointments.exists():
            raise ValidationError(
                "This appointment slot is unavailable. Please choose a "
                "different time."
            )

    def save(self, *args, **kwargs):
        # Calls the full_clean method to ensure form validations are run
        # before saving
        self.full_clean()
        super(Appointment, self).save(*args, **kwargs)
