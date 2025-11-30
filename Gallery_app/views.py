from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Album, Image, Comment, Like
from django.views import View
from django.contrib import messages




@login_required
def album_list(request):
    albums = Album.objects.filter(user=request.user)
    return render(request, "gallery/album_list.html", {"albums": albums})

@login_required
def album_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        cover = request.FILES.get("cover_image")

        Album.objects.create(
            title=title,
            description=description,
            cover_image=cover,
            user=request.user
        )
        return redirect("album_list")

    return render(request, "gallery/album_create.html")

@login_required
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk, user=request.user)
    return render(request, "gallery/album_detail.html", {"album": album})


@login_required
def image_list(request):
    images = Image.objects.filter(user=request.user)
    return render(request, "gallery/image_list.html", {"images": images})


@login_required
def image_upload(request):
    albums = Album.objects.filter(user=request.user)

    if request.method == "POST":
        Image.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            image=request.FILES.get("image"),
            album_id=request.POST.get("album") or None,
            user=request.user
        )
        return redirect("image_list")

    return render(request, "gallery/image_upload.html", {"albums": albums})


@login_required
def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    comments = image.comments.all()
    return render(request, "gallery/image_detail.html", {"image": image, "comments": comments})


@login_required
def add_comment(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    if request.method == "POST":
        Comment.objects.create(
            image=image,
            user=request.user,
            name=request.POST.get("name"),
            description=request.POST.get("description")
        )
        return redirect("image_detail", pk=image_id)


@login_required
def toggle_like(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    like = Like.objects.filter(user=request.user, image=image)

    if like.exists():
        like.delete()
        return JsonResponse({"status": "unliked", "likes": image.likes.count()})

    Like.objects.create(user=request.user, image=image)
    return JsonResponse({"status": "liked", "likes": image.likes.count()})