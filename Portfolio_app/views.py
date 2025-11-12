from django.shortcuts import render
from django.views.generic import ListView
from .models import Portfolio

class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = "portfolios"
    template_name = "Portfolio_app/portfoliolist.html"

# Create your views here.
