from django import forms
from .models import Portfolio, PortfolioImages

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["name", "discription", "link", "file"]