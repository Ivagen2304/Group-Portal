from django.db import models

# Create your models here.
class Advertisement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_limit = models.DateField(null = True, blank=True)

class List(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_limit = models.DateField(null = True, blank=True)