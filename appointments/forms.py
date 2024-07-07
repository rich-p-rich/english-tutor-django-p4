from django import forms
from .models import Appointment

# Form: book appointments:
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'surname', 'email', 'meeting_date', 'meeting_time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'meeting_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Date', 'type': 'date'}),
            'meeting_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Time', 'type': 'time'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }

# Form: search appointments to choose one to change
class SearchAppointmentsForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}))

# Form: change the appointment 
class ChangeAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['meeting_date', 'meeting_time']
        widgets = {
            'meeting_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'meeting_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }