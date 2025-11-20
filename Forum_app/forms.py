from django import forms
from .models import Category, Topic, Message


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['category', 'title', 'is_closed']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['topic', 'text']