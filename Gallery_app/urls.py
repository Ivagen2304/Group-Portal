from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_home, name='gallery_home'),
    path('albums/', views.album_list, name='album_list'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('image/<int:image_id>/', views.image_detail, name='image_detail'),
    path('image/<int:image_id>/like/', views.like_image, name='like_image'),
    path('image/<int:image_id>/comment/', views.add_comment, name='add_comment'),
]