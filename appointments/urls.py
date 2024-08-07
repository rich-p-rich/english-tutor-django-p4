from . import views
from django.urls import path

urlpatterns = [
    path('', views.make_appointment,
         name='appointments'),
    path('confirmation/', views.confirm_appointment, name='confirmation'),
    path('manage-appointments/', views.manage_appointments,
         name='manage_appointments'),
]
