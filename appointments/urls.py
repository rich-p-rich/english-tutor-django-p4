from . import views
from django.urls import path   

urlpatterns = [
    path('', views.make_appointment, name='appointments'),
    path('', views.confirm_appointment, name='appointments-confirmation'),
]