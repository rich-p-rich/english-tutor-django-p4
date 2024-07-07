from . import views
from django.urls import path   

urlpatterns = [
    path('', views.make_appointment, name='appointments'),
    path('confirmation/', views.confirm_appointment, name='confirmation'),
    path('change/', views.change_appointment, name='change'),
    path('change/', views.change_appointment, name='change_appointment'),
]