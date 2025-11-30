from django.urls import path
from .views import login_view, register_view, logout_view, profile_view

urlpatterns = [
    path("", login_view, name="auth_home"),   # ← теперь /auth/ будет вести на логин
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
]
