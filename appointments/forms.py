from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Appointment, MAX_APPOINTMENT_WEEKS, MIN_APPOINTMENT_DAYS

class AppointmentForm(forms.ModelForm):
    """
    For booking appointments
    """
    meeting_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)

    class Meta:
        model = Appointment
        fields = ['name', 'surname', 'email', 'meeting_date', 'meeting_time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'meeting_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Time', 'type': 'time'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }

    def clean_meeting_date(self):
        meeting_date = self.cleaned_data['meeting_date']
        today = timezone.now().date()
        min_date = today + timedelta(days=MIN_APPOINTMENT_DAYS)
        max_date = today + timedelta(weeks=MAX_APPOINTMENT_WEEKS)
        
        if not (min_date <= meeting_date <= max_date):
            raise forms.ValidationError(f"Please choose a date between {min_date} and {max_date}.")
        
        return meeting_date
    
    def clean_name(self):
        name = self.cleaned_data.get('name').strip().title()
        return name

    def clean_surname(self):
        surname = self.cleaned_data.get('surname').strip().title()
        return surname

class SearchAppointmentsForm(forms.Form):
    """
    Form for searching appointments to choose one to change
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}))

    def clean_email(self):
        email = self.cleaned_data.get('email').strip().lower()
        return email

    def clean_surname(self):
        surname = self.cleaned_data.get('surname').strip().lower()
        return surname

class ChangeAppointmentForm(forms.ModelForm):
    """
    Form for changing the appointment
    """
    meeting_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)

    class Meta:
        model = Appointment
        fields = ['meeting_date', 'meeting_time']
        widgets = {
            'meeting_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

    def clean_meeting_date(self):
        meeting_date = self.cleaned_data['meeting_date']
        today = timezone.now().date()
        min_date = today + timedelta(days=MIN_APPOINTMENT_DAYS)
        max_date = today + timedelta(weeks=MAX_APPOINTMENT_WEEKS)
        
        if not (min_date <= meeting_date <= max_date):
            raise forms.ValidationError(f"Please choose a date between {min_date} and {max_date}.")
        
        return meeting_date