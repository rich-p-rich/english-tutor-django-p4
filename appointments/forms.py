from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'meeting_date', 'meeting_time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'meeting_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Date', 'type': 'date'}),
            'meeting_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Time', 'type': 'time'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }

class SearchAppointmentsForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}))