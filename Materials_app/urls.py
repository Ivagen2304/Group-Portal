from django.urls import path
from . import views

urlpatterns = [
    path("", views.material_list, name="material_list"),
    path("material/<int:pk>/", views.material_detail, name="material_detail"),
    path("material/create/", views.material_create, name="material_create"),
    path("material/<int:pk>/update/", views.material_update, name="material_update"),
    path("material/<int:pk>/delete/", views.material_delete, name="material_delete"),

    path("categories/", views.category_list, name="material_category_list"),
    path("categories/create/", views.category_create, name="material_category_create"),
    path("categories/<int:pk>/update/", views.category_update, name="material_category_update"),
    path("categories/<int:pk>/delete/", views.category_delete, name="material_category_delete"),
]
