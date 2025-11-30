from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Image, Album


# Главная страница галереи
def gallery_home(request):
    return render(request, "Gallery_app/gallery_home.html")


# Список альбомов
def album_list(request):
    albums = Album.objects.all()
    return render(request, "Gallery_app/album_list.html", {"albums": albums})


# Детальная страница альбома
def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    images = album.images.all()  # если связь ManyToMany
    return render(request, "Gallery_app/album_detail.html", {
        "album": album,
        "images": images
    })


# Детальная страница изображения
def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, "Gallery_app/image_detail.html", {"image": image})


# Лайк изображения (заглушка)
def like_image(request, image_id):
    return HttpResponse("Лайк подтверждён!")  


# Комментарий к изображению (заглушка)
def add_comment(request, image_id):
    return HttpResponse("Комментарий добавлен!")  
