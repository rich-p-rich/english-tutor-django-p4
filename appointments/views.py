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
    return render(request, 'appointments/appt-confirmation.html', {'appointment': appointment_details})

# View for changing appointments
def search_and_edit_appointments(request):
    # This enables the user to search their appointments
    search_form = SearchAppointmentsForm()
    change_form = None
    appointments = None
    appointment_to_edit = None

    if request.method == 'POST':
        if 'search' in request.POST:
            search_form = SearchAppointmentsForm(request.POST)
            if search_form.is_valid():
                # The search fields:
                email = search_form.cleaned_data['email']
                surname = search_form.cleaned_data['surname']
                appointments = Appointment.objects.filter(email=email, surname=surname)
        elif 'select' in request.POST:
            appointment_id = request.POST.get('appointment_id')
            appointment_to_edit = get_object_or_404(Appointment, id=appointment_id)
            # Cross reference to forms.py -> Change Appointment Form
            change_form = ChangeAppointmentForm(instance=appointment_to_edit)
        elif 'save' in request.POST:
            appointment_id = request.POST.get('appointment_id')
            appointment_to_edit = get_object_or_404(Appointment, id=appointment_id)
            change_form = ChangeAppointmentForm(request.POST, instance=appointment_to_edit)
            if change_form.is_valid():
                change_form.save()
                # Display change confirmation
                return render(request, 'appointments/change-confirmed.html', {'appointment': appointment_to_edit})

    return render(request, 'appointments/search_and_edit.html', {
        'search_form': search_form,
        'change_form': change_form,
        'appointments': appointments,
        'appointment_to_edit': appointment_to_edit
    })