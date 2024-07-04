from django.shortcuts import render, redirect
from django.views import generic
from .models import Appointment
from .forms import AppointmentForm
import datetime

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_confirmation')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

    """
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            timezone = request.POST['timezone']
            meeting_date = request.POST['meeting_date']
            meeting_time = request.POST['meeting_time']
            message = request.POST['message']

            meeting_datetime = datetime.datetime.strptime(f"{meeting_date} {meeting_time}", "%Y-%m-%d %H:%M:%S")

            # Create the meeting
            meeting = Appointment.objects.create(
                name=name,
                email=email,
                timezone=timezone,
                meeting_date=meeting_date,
                meeting_time=meeting_time,
                message=message
            )
            return HttpResponse(f"Meeting scheduled successfully with ID: {meeting.id}")
            """

