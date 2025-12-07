from django.urls import path
from .views import (
    ListListView, ListDetailView, ListCreateView,
    ListUpdateView, ListDeleteView,
    AdvertisementListView, AdvertisementDetailView,
    AdvertisementCreateView, AdvertisementUpdateView,
    AdvertisementDeleteView
)

urlpatterns = [
    # Lists
    path("lists/", ListListView.as_view(), name="list_list"),
    path("lists/create/", ListCreateView.as_view(), name="list_create"),
    path("lists/<int:pk>/", ListDetailView.as_view(), name="list_detail"),
    path("lists/<int:pk>/update/", ListUpdateView.as_view(), name="list_update"),
    path("lists/<int:pk>/delete/", ListDeleteView.as_view(), name="list_delete"),

    # Advertisements
    path("", AdvertisementListView.as_view(), name="advertisement_list"),
    path("create/", AdvertisementCreateView.as_view(), name="advertisement_create"),
    path("<int:pk>/", AdvertisementDetailView.as_view(), name="advertisement_detail"),
    path("<int:pk>/update/", AdvertisementUpdateView.as_view(), name="advertisement_update"),
    path("<int:pk>/delete/", AdvertisementDeleteView.as_view(), name="advertisement_delete"),
]
