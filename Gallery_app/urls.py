from django.urls import path
from . import views

urlpatterns = [
    path("albums/", views.album_list, name="album_list"),
    path("albums/create/", views.album_create, name="album_create"),
    path("albums/<int:pk>/", views.album_detail, name="album_detail"),
    path("images/", views.image_list, name="image_list"),
    path("images/upload/", views.image_upload, name="image_upload"),
    path("images/<int:pk>/", views.image_detail, name="image_detail"),
    path("images/<int:image_id>/comment/", views.add_comment, name="add_comment"),
    path("images/<int:image_id>/like/", views.toggle_like, name="toggle_like"),
]