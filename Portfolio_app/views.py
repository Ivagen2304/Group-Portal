from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Portfolio
from .forms import PortfolioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserIsOwnerMixin

class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = "portfolios"
    template_name = "Portfolio_app/portfoliolist.html"

class PortfolioDetail(DetailView):
    model = Portfolio
    context_object_name = "portfolio"
    template_name = "Portfolio_app/portfoliodetail.html"

class PortfolioCreate(LoginRequiredMixin, CreateView):
    model = Portfolio
    context_object_name = "portfolio"
    template_name = "Portfolio_app/portfoliocreate.html"
    form_class = PortfolioForm
    success_url = "/portfolio/"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
class PortfolioUpdate(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Portfolio
    context_object_name = "portfolio"
    template_name = "Portfolio_app/portfolioupdate.html"
    form_class = PortfolioForm
    success_url = "/portfolio/"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
class PortfolioDelete(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Portfolio
    context_object_name = "portfolio"
    template_name = "Portfolio_app/portfoliodelete.html"
    form_class = PortfolioForm
    success_url = "/portfolio/"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
# Create your views here.
