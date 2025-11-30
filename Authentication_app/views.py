from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")  # куда отправить после входа
    else:
        form = AuthenticationForm()
    return render(request, "Authentication_app/login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "Authentication_app/register.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "Authentication_app/profile.html")


def logout_view(request):
    logout(request)
    return redirect("login")
