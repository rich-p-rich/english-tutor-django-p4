from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home/home.html'

#class HomePage(generic.TemplateView):
 #   """
  #  Renders the Home Page index.html
   # """
    #template_name = 'home/index.html'