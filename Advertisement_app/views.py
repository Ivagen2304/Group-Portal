
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'  
    context_object_name = 'advertisements' 

class ListListView(ListView):
    model = List
    template_name = 'Advertisement_app/list_adverisement.html'  # без "Advertisement_app/"
    context_object_name = 'listes'



