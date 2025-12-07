from django import forms
from .models import Advertisement, AdvertisementList


class AdvertisementForm(forms.ModelForm):
    deadline = forms.DateField(
        label="Дедлайн",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Advertisement
        fields = ["title", "content", "deadline", "list"]


class ListForm(forms.ModelForm):
    deadline = forms.DateField(
        label="Дедлайн",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = AdvertisementList
        fields = ["name", "description", "deadline"]
