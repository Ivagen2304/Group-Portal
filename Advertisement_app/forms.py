from django import forms
from .models import Advertisement, List

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'content']


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'description', 'date_limit']
