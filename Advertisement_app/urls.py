from django.urls import path
from .views import AdvertisementListView, ListListView

urlpatterns = [
    path('', AdvertisementListView.as_view(), name='advertisement_list'),
    path('listes/', ListListView.as_view(), name='list_advertisement'),
]
