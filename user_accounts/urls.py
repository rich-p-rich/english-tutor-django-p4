from django.urls import path
from .views import custom_sign_in, custom_register_account

urlpatterns = [
    path('sign-in/', custom_sign_in, name='sign_in'),
    path('register/', custom_register_account, name='account_signup'),
    ]