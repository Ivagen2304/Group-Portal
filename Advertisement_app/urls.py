from django.urls import path
from .views import (
    AdvertisementListView, AdvertisementDetailView,
    AdvertisementCreateView, AdvertisementUpdateView, AdvertisementDeleteView,

    ListListView, ListDetailView, ListCreateView,
    ListUpdateView, ListDeleteView
)

urlpatterns = [
    # --- Advertisements ---
    path('', AdvertisementListView.as_view(), name='advertisement_list'),
    path('<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('create/', AdvertisementCreateView.as_view(), name='advertisement_create'),
    path('update/<int:pk>/', AdvertisementUpdateView.as_view(), name='advertisement_update'),
    path('delete/<int:pk>/', AdvertisementDeleteView.as_view(), name='advertisement_delete'),

    # --- Listes ---
    path('listes/', ListListView.as_view(), name='list_list'),
    path('listes/<int:pk>/', ListDetailView.as_view(), name='list_detail'),
    path('listes/create/', ListCreateView.as_view(), name='list_create'),
    path('listes/update/<int:pk>/', ListUpdateView.as_view(), name='list_update'),
    path('listes/delete/<int:pk>/', ListDeleteView.as_view(), name='list_delete'),
]
