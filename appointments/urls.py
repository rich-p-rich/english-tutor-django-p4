from . import views
from django.urls import path   

urlpatterns = [
    path('', views.book_appointment, name='appointments'),
]