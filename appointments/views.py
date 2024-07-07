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

# View for searching and editing appointments
def search_and_edit_appointments(request):
    if 'search' in request.POST:
        return search_appointments(request)
    elif 'select' in request.POST or 'save' in request.POST:
        return edit_appointment(request)
    else:
        return render(request, 'appointments/search_and_edit.html', {
            'search_form': SearchAppointmentsForm(),
            'change_form': None,
            'appointments': None,
            'appointment_to_edit': None
        })

# View for searching appointments
def search_appointments(request):
    search_form = SearchAppointmentsForm(request.POST)
    appointments = None

    if search_form.is_valid():
        email = search_form.cleaned_data['email']
        surname = search_form.cleaned_data['surname']
        appointments = Appointment.objects.filter(email=email, surname=surname)

    return render(request, 'appointments/search_and_edit.html', {
        'search_form': search_form,
        'appointments': appointments,
        'change_form': None,
        'appointment_to_edit': None
    })

# View for changing appointments
def edit_appointment(request):
    appointment_to_edit = None
    change_form = None

    if 'select' in request.POST:
        appointment_id = request.POST.get('appointment_id')
        appointment_to_edit = get_object_or_404(Appointment, id=appointment_id)
        change_form = ChangeAppointmentForm(instance=appointment_to_edit)
    elif 'save' in request.POST:
        appointment_id = request.POST.get('appointment_id')
        appointment_to_edit = get_object_or_404(Appointment, id=appointment_id)
        change_form = ChangeAppointmentForm(request.POST, instance=appointment_to_edit)
        if change_form.is_valid():
            change_form.save()
            return render(request, 'appointments/confirmation.html', {'appointment': appointment_to_edit})

    return render(request, 'appointments/search_and_edit.html', {
        'search_form': SearchAppointmentsForm(),
        'appointments': None,
        'change_form': change_form,
        'appointment_to_edit': appointment_to_edit
    })