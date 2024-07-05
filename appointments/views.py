from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm


def appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_confirmation')
    else:
        form = AppointmentForm()
    return render(request, 'appointments.html', {'form': form})
