from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment
import datetime

# Create your views here.

def my_appointments(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        timezone = request.POST['timezone']
        meeting_date = request.POST['meeting_date']
        meeting_time = request.POST['meeting_time']
        message = request.POST['message']

        # Parse the date and time
        meeting_datetime = datetime.datetime.strptime(f"{meeting_date} {meeting_time}", "%Y-%m-%d %H:%M:%S")

        # Create the meeting
        meeting = Meeting.objects.create(
            name=name,
            email=email,
            timezone=timezone,
            meeting_date=meeting_date,
            meeting_time=meeting_time,
            message=message
        )
        return HttpResponse(f"Meeting scheduled successfully with ID: {meeting.id}")

    return render(request, 'appointments/schedule_meeting.html')