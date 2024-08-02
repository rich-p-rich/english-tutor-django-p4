from django.shortcuts import render, redirect, get_object_or_404
from user_accounts.models import UserProfile
from .models import Appointment
from .forms import AppointmentForm, ChangeAppointmentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages 
from django.core.exceptions import ValidationError


@login_required
@csrf_protect
def make_appointment(request):
    """
    View for main appointments page -> book a call
    """
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user_profile = user_profile
            try:
                appointment.save()
                request.session['appointment_date'] = str(appointment.meeting_date)
                request.session['appointment_time'] = str(appointment.meeting_time)
                return redirect('confirmation')
            except ValidationError as e:
                form.add_error(None, e.message)
    else:
        form = AppointmentForm()
    
    return render(request, 'appointments/book-appointments.html', {'form': form})

@login_required
def confirm_appointment(request):
    """
    View for appointment confirmation page
    """
    appointment_details = {
        'email': request.session.get('appointment_email'),
        'date': request.session.get('appointment_date'),
        'time': request.session.get('appointment_time')
    }
    return render(request, 'appointments/appointment-confirmed.html', {'appointment': appointment_details})

@login_required
def manage_appointments(request):
    """
    View for managing appointments -> allows user to see all their appointments and edit or cancel them
    """
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    appointments = Appointment.objects.filter(user_profile=user_profile)
    change_form = None
    appointment_to_edit = None

    if request.method == 'POST':
        if 'select' in request.POST:
            appointment_id = request.POST.get('appointment_id')
            appointment_to_edit = get_object_or_404(Appointment, id=appointment_id)
            change_form = ChangeAppointmentForm(instance=appointment_to_edit)
        elif 'save' in request.POST:
            appointment_id = request.POST.get('appointment_id')
            appointment_to_edit = get_object_or_404(Appointment, id=appointment_id)
            change_form = ChangeAppointmentForm(request.POST, instance=appointment_to_edit)
            if change_form.is_valid():
                try:
                    change_form.save()
                    return render(request, 'appointments/change-confirmed.html', {'appointment': appointment_to_edit})
                except ValidationError as e:
                    change_form.add_error(None, e.message)
        elif 'confirm_cancel' in request.POST:
            appointment_id = request.POST.get('appointment_id')
            appointment_to_cancel = get_object_or_404(Appointment, id=appointment_id)
            appointment_to_cancel.delete()
            return render(request, 'appointments/cancellation-confirmed.html', {'appointment': appointment_to_cancel})

    return render(request, 'appointments/change-or-cancel.html', {
        'appointments': appointments,
        'change_form': change_form,
        'appointment_to_edit': appointment_to_edit
    })