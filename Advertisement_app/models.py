from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class List(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_limit = models.DateField(null = True, blank=True)