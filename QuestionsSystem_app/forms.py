from django import forms
from .models import Question, Answer, Category

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "text", "category"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
