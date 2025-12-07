from django.urls import path
from . import views

urlpatterns = [
    path("", views.poll_list, name="poll_list"),
    path("create/", views.poll_create, name="poll_create"),
    path("<int:poll_id>/edit/", views.poll_edit, name="poll_edit"),
    path("<int:poll_id>/add-option/", views.poll_add_option, name="poll_add_option"),
    path("<int:poll_id>/vote/", views.poll_vote, name="poll_vote"),
    path("<int:poll_id>/results/", views.poll_results, name="poll_results"),
]
