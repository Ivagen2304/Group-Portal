from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Image, Album


def gallery_home(request):
    return render(request, "Gallery_app/gallery_home.html")


def album_list(request):
    albums = Album.objects.all()
    return render(request, "Gallery_app/album_list.html", {"albums": albums})


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    images = album.images.all()
    return render(request, "Gallery_app/album_detail.html", {
        "album": album,
        "images": images
    })



def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, "Gallery_app/image_detail.html", {"image": image})



def like_image(request, image_id):
    return HttpResponse("Лайк подтверждён!")  



def add_comment(request, image_id):
    return HttpResponse("Комментарий добавлен!")  
