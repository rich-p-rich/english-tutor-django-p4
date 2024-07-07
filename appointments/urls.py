from . import views
from django.urls import path   

urlpatterns = [
    path('', views.make_appointment, name='appointments'),
    path('confirmation/', views.confirm_appointment, name='confirmation'),
    path('search_and_edit/', views.search_and_edit_appointments, name='search_and_edit_appointments'),
]