from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    name = models.CharField(max_length = 20)
    discription = models.TextField()
    creator = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
        
class PortfolioImages(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = "portfolio/")


# Create your models here.
