from django.shortcuts import render,HttpResponse
from django.template import loader
from django.views.generic import TemplateView, View

# Create your views here.
class Home(TemplateView):
    template_name = 'pages/index.html'

class About(TemplateView):
    template_name = 'pages/about.html'

class Services(TemplateView):
    template_name = 'pages/services.html'

class Gallery(TemplateView):
    template_name = 'pages/gallery.html'

class Typo(TemplateView):
    template_name = 'pages/typo.html'