from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["name", "discription", "link", "file"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Например: Мій перший сайт / Мой первый сайт",
                }
            ),
            "discription": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Коротко опиши, що це за робота / что это за работа",
                }
            ),
            "link": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://… (опционально)",
                }
            ),
            "file": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
