from django import forms
from .models import Material, MaterialCategory


class MaterialCategoryForm(forms.ModelForm):
    class Meta:
        model = MaterialCategory
        fields = ["name"]
        labels = {
            "name": "Назва розділу",
        }


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["title", "description", "subject", "school_class", "category", "file"]
        labels = {
            "title": "Назва",
            "description": "Опис",
            "subject": "Предмет",
            "school_class": "Клас",
            "category": "Розділ",
            "file": "Файл",
        }
