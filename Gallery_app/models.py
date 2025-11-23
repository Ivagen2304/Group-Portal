from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="gallery/albums/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="albums")

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gallery_images")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="images", null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gallery_comments")
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.image.name}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'image')

