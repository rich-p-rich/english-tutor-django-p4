from . import views
from django.urls import path   

urlpatterns = [
    path('appointments/', book_appointment, name='appointments'),
    path('appointment-confirmation/', TemplateView.as_view(template_name='appointment_confirmation.html'), name='appointment_confirmation.html'),
]