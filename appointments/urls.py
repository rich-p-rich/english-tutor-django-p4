from . import views
from django.urls import path   

urlpatterns = [
    path('', views.AppointmentsView.as_view(), name='appointments'),
    path('book-appointment/', book_appointment, name='book_appointment'),
    path('appointment-success/', TemplateView.as_view(template_name='appointment_success.html'), name='appointment_success'),
]
