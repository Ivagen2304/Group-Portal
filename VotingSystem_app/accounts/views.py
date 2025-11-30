from django.shortcuts import render, redirect
from .forms import RoleChoiceForm, RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import User

def index(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    return render(request, 'accounts/index.html')

def register_choice(request):
    if request.method == 'POST':
        form = RoleChoiceForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            # redirect to register with role in GET
            return redirect(f"{reverse('accounts:register')}?role={role}")
    else:
        form = RoleChoiceForm()
    return render(request, 'accounts/register_choice.html', {'form': form})

def register(request):
    role = request.GET.get('role', 'user')  # за замовчуванням user

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Паролі не збігаються")
            return redirect(request.path + f"?role={role}")
        
        if role == 'moderator':
            code = request.POST.get('moderator_code', '')
            if code != settings.MODERATOR_CODE:
                messages.error(request, "Невірний код модератора")
                return redirect(request.path + f"?role={role}")
            is_moderator = True
        else:
            is_moderator = False

        # Створення користувача
        user = User.objects.create_user(username=username, password=password1, is_moderator=is_moderator)
        messages.success(request, "Реєстрація успішна!")
        return redirect('accounts:login')

    return render(request, "accounts/register.html", {"role": role})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_suspended():
                messages.error(request, 'Ваш акаунт тимчасово заблокований.')
                return redirect('accounts:login')
            login(request, user)
            return redirect('accounts:home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    """
    Вихід з аккаунту — знищує сесію та редиректить на сторінку вибору реєстрації/входу.
    Приймає POST або GET (безпека: краще використовувати POST у формі).
    """
    # Виконуємо вихід
    logout(request)
    # Переадресація на сторінку вибору реєстрації/входу
    return redirect('accounts:register_choice')

@login_required
def home(request):
    return render(request, 'accounts/home.html')
