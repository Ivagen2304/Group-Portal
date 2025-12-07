from django.urls import path
from . import views

urlpatterns = [
    path("", views.question_list, name="question_list"),

    path("category/<int:pk>/", views.category_detail, name="category_detail"),
    path("category/create/", views.category_create, name="category_create"),

    path("question/<int:pk>/", views.question_detail, name="question_detail"),
    path("question/create/", views.question_create, name="question_create"),
    path("question/<int:pk>/update/", views.question_update, name="question_update"),
    path("question/<int:pk>/delete/", views.question_delete, name="question_delete"),
]
