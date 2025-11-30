from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.conf import settings

class RoleChoiceForm(forms.Form):
    ROLE_CHOICES = (('user','Звичайний користувач'),('moderator','Модератор'))
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect, label='Який у вас статус?')

class RegisterForm(UserCreationForm):
    role = forms.CharField(widget=forms.HiddenInput(), required=False)
    moderator_code = forms.CharField(required=False, label='Код модератора')

    class Meta:
        model = User
        fields = ('username','password1','password2')

    def clean(self):
        cleaned = super().clean()
        role = self.data.get('role')
        code = cleaned.get('moderator_code')
        if role == 'moderator':
            expected = getattr(settings, 'MODERATOR_CODE', None)
            if not expected or code != expected:
                raise forms.ValidationError('Невірний код модератора')
        return cleaned

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Нікнейм')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
