from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    """
    Renders the Home Page index.html
    """
    template_name = 'index.html'