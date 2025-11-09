from .views import CategoryListView
from django.urls import path, include


urlpatterns = [
    path('', CategoryListView.as_view(), name='categorylist')
]