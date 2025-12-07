from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Material, MaterialCategory
from .forms import MaterialForm, MaterialCategoryForm


def material_list(request):
    """
    Главная страница материалов:
    - сверху фильтры: предмет, класс, раздел
    - ниже карточки материалов
    """
    materials = Material.objects.all()
    categories = MaterialCategory.objects.all()

    # Фильтры из GET-параметров
    subject = request.GET.get("subject")
    school_class = request.GET.get("class")
    category_id = request.GET.get("category")

    if subject:
        materials = materials.filter(subject__icontains=subject)
    if school_class:
        materials = materials.filter(school_class__icontains=school_class)
    if category_id:
        materials = materials.filter(category_id=category_id)

    return render(request, "Materials_app/material_list.html", {
        "materials": materials,
        "categories": categories,
        "subject": subject or "",
        "school_class": school_class or "",
        "selected_category": int(category_id) if category_id else None,
    })


def material_detail(request, pk):
    """
    Страница одного материала (карточка + кнопка скачать)
    """
    material = get_object_or_404(Material, pk=pk)
    return render(request, "Materials_app/material_detail.html", {
        "material": material
    })


@login_required
def material_create(request):
    """
    Создание материала – только для авторизованных
    """
    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("material_list")
    else:
        form = MaterialForm()
    return render(request, "Materials_app/material_form.html", {
        "form": form,
        "title": "Створити матеріал",
    })


@login_required
def material_update(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect("material_detail", pk=material.pk)
    else:
        form = MaterialForm(instance=material)
    return render(request, "Materials_app/material_form.html", {
        "form": form,
        "title": "Редагувати матеріал",
    })


@login_required
def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        material.delete()
        return redirect("material_list")
    return render(request, "Materials_app/material_delete.html", {
        "material": material
    })


# ====== КАТЕГОРИИ ======


def category_list(request):
    categories = MaterialCategory.objects.all()
    return render(request, "Materials_app/category_list.html", {
        "categories": categories
    })


@login_required
def category_create(request):
    if request.method == "POST":
        form = MaterialCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("material_category_list")
    else:
        form = MaterialCategoryForm()
    return render(request, "Materials_app/category_form.html", {
        "form": form,
        "title": "Створити розділ",
    })


@login_required
def category_update(request, pk):
    category = get_object_or_404(MaterialCategory, pk=pk)
    if request.method == "POST":
        form = MaterialCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("material_category_list")
    else:
        form = MaterialCategoryForm(instance=category)
    return render(request, "Materials_app/category_form.html", {
        "form": form,
        "title": "Редагувати розділ",
    })


@login_required
def category_delete(request, pk):
    category = get_object_or_404(MaterialCategory, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("material_category_list")
    return render(request, "Materials_app/category_delete.html", {
        "category": category
    })
