from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class Image(ListView):
    model = Image
    #context_object_name = 
    #template_name = 
