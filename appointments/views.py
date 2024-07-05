from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment-confirmation')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointments.html', {'form': form})
