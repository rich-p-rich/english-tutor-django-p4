from . import views
from django.urls import path   

urlpatterns = [
    path('', views.make_appointment, name='appointments'),
    path('confirmation/', views.confirm_appointment, name='confirmation'),
    path('search/', views.search_appointments, name='search_appointments'),
]