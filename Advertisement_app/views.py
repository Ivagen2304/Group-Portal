from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from .models import Advertisement, AdvertisementList
from .forms import AdvertisementForm, ListForm


# ===== LISTS =====

class ListListView(ListView):
    model = AdvertisementList
    template_name = "Advertisement_app/list_list.html"
    context_object_name = "lists"


class ListDetailView(DetailView):
    model = AdvertisementList
    template_name = "Advertisement_app/list_detail.html"
    context_object_name = "list"


class ListCreateView(CreateView):
    model = AdvertisementList
    form_class = ListForm
    template_name = "Advertisement_app/list_form.html"
    success_url = reverse_lazy("list_list")


class ListUpdateView(UpdateView):
    model = AdvertisementList
    form_class = ListForm
    template_name = "Advertisement_app/update.html"
    success_url = reverse_lazy("list_list")


class ListDeleteView(DeleteView):
    model = AdvertisementList
    template_name = "Advertisement_app/list_delete.html"
    success_url = reverse_lazy("list_list")


# ===== ADVERTISEMENTS =====

class AdvertisementListView(ListView):
    model = Advertisement
    template_name = "Advertisement_app/advertisement_list.html"
    context_object_name = "advertisements"


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = "Advertisement_app/advertisement_detail.html"
    context_object_name = "advertisement"


class AdvertisementCreateView(CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "Advertisement_app/advertisement_create.html"
    success_url = reverse_lazy("advertisement_list")


class AdvertisementUpdateView(UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "Advertisement_app/advertisement_update.html"
    success_url = reverse_lazy("advertisement_list")


class AdvertisementDeleteView(DeleteView):
    model = Advertisement
    template_name = "Advertisement_app/advertisement_delete.html"
    success_url = reverse_lazy("advertisement_list")
