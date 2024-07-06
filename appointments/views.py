from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
# View for main appointments page -> book a call
def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment-confirmation')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointments.html', {'form': form})

# View for appointment confirmation 
def confirm_appointment(request):
    appointment = get_object_or_404(Appointment)
    return render(request, 'appointments/appointment-confirmation.html', {'appointment': appointment})

# View for change or cancel a call 
