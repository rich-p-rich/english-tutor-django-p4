from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm, SearchAppointmentsForm, ChangeAppointmentForm
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
def search_appointments(request):
    search_form = SearchAppointmentsForm()
    appointments = None

    if request.method == 'POST':
        search_form = SearchAppointmentsForm(request.POST)
        if search_form.is_valid():
            email = search_form.cleaned_data['email']
            surname = search_form.cleaned_data['surname']
            appointments = Appointment.objects.filter(email=email, surname=surname)

    return render(request, 'appointments/search.html', {
        'search_form': search_form,
        'appointments': appointments
    })

# View for changing date and / time of a call
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        change_form = ChangeAppointmentForm(request.POST, instance=appointment)
        if change_form.is_valid():
            change_form.save()
            return render(request, 'appointments/confirmation.html', {'appointment': appointment})
    else:
        change_form = ChangeAppointmentForm(instance=appointment)
    
    return render(request, 'appointments/edit.html', {
        'change_form': change_form,
        'appointment': appointment
    })

# View for cancelling a call 
