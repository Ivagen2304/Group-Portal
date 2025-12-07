from django import forms
from .models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
