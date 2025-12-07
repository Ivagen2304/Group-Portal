from django import forms
from .models import Event, EventMedia


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "date", "cover"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
            "cover": forms.FileInput(attrs={"class": "form-control"}),
        }


class MediaForm(forms.ModelForm):
    class Meta:
        model = EventMedia
        fields = ["file"]

        widgets = {
            "file": forms.FileInput(attrs={"class": "form-control"}),
        }
