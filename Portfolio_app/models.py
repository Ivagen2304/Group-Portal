from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    name = models.CharField(max_length = 20)
    discription = models.TextField()
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    link = models.CharField(max_length = 1000, blank = True, null = True)
    file = models.FileField(upload_to = "portfoliofiles/", blank = True, null = True)

    def __str__(self):
        return self.name
        
class PortfolioImages(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = "portfolio/")



# Create your models here.
