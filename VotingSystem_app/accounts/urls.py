from django.urls import path
from . import views
from .views import user_logout
app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('register-choice/', views.register_choice, name='register_choice'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', user_logout, name='logout'),
]
