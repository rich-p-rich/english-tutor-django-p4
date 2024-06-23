from django.shortcuts import render
from django.views import generic

# Create your views here.

class HomePage(generic.TemplateView):
    """
    Renders the Home Page index.html
    """
    template_name = 'home/index.html'