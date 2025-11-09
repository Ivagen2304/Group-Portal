from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categoryes'
    template_name = 'Forum_app/categorylist.html'