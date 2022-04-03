from pyexpat import model
from django.db import models

# Create your models here.


class City(models.Model):
    cityName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.cityName
