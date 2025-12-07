from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    cover = models.ImageField(upload_to="event_covers/", blank=True, null=True)

    def __str__(self):
        return self.title


class EventMedia(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="media")
    file = models.FileField(upload_to="event_media/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def is_image(self):
        return self.file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))

    def is_video(self):
        return self.file.name.lower().endswith(('.mp4', '.mov', '.avi', '.webm'))

    def __str__(self):
        return f"Media for {self.event.title}"
