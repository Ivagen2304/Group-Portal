from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Portfolio
from .forms import PortfolioForm


class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = "portfolios"
    template_name = "Portfolio_app/portfoliolist.html"
    paginate_by = 10
    ordering = ["-id"]  # последние сверху


class PortfolioDetail(DetailView):
    model = Portfolio
    context_object_name = "portfolio"
    template_name = "Portfolio_app/portfoliodetail.html"


class PortfolioCreate(LoginRequiredMixin, CreateView):
    model = Portfolio
    form_class = PortfolioForm
    context_object_name = "portfolio"
    template_name = "Portfolio_app/portfoliocreate.html"
    success_url = reverse_lazy("portfoliolist")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class PortfolioUpdate(LoginRequiredMixin, UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    context_object_name = "portfolio"
    template_name = "Portfolio_app/portfolioupdate.html"
    success_url = reverse_lazy("portfoliolist")

    # Разрешаем редактировать только авторам и суперюзеру
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            return qs
        return qs.filter(creator=user)


class PortfolioDelete(LoginRequiredMixin, DeleteView):
    model = Portfolio
    context_object_name = "portfolio"
    template_name = "Portfolio_app/portfoliodelete.html"
    success_url = reverse_lazy("portfoliolist")

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            return qs
        return qs.filter(creator=user)
