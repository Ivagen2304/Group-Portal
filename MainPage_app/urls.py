from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #path('', TemplateView.as_view(template_name='MainPage_app/main_page.html')),
    path('', views.main_page, name='main_page'),

    
]

