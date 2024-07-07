from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm, SearchAppointmentsForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
# View for main appointments page -> book a call
def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            request.session['appointment_email'] = appointment.email
            request.session['appointment_date'] = str(appointment.meeting_date)
            request.session['appointment_time'] = str(appointment.meeting_time)
            return redirect('confirmation')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointments.html', {'form': form})

# View for appointment confirmation page
def confirm_appointment(request):
    appointment_details = {
        'email': request.session.get('appointment_email'),
        'date': request.session.get('appointment_date'),
        'time': request.session.get('appointment_time')
    }
    return render(request, 'appointments/confirmation.html', {'appointment': appointment_details})

# View for searching a booked call based on surname and email 
def change_appointments(request):
    form = SearchAppointmentsForm()
    appointments = None
    if request.method == 'POST':
        form = SearchAppointmentsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            surname = form.cleaned_data['surname']
            appointments = Appointment.objects.filter(email=email, surname=surname)
    return render(request, 'appointments/change.html', {'form': form, 'appointments': appointments})

# View for changing date and / time of a call
def change_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = EditAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = EditAppointmentForm(instance=appointment)
    return render(request, 'appointments/edit_appointment.html', {'form': form, 'appointment': appointment})

# View for cancelling a call 
