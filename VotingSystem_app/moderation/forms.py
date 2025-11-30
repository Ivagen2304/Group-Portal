from django import forms
from .models import Poll, PollOption
from django.forms import formset_factory

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']

class OptionForm(forms.Form):
    text = forms.CharField(max_length=256, label='Варіант відповіді')

OptionFormSet = formset_factory(OptionForm, extra=2, max_num=10, validate_max=True)
