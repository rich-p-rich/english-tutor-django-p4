from django.urls import path
from .views import custom_sign_in

urlpatterns = [
    path('sign-in/', custom_sign_in, name='sign_in'),
    ]