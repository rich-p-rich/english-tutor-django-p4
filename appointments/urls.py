from . import views
from django.urls import path   

urlpatterns = [
    path('', views.AppointmentsView.as_view(), name='appointments'),
]
