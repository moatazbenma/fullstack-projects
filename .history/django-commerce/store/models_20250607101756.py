from django.db import models
from django.db import 
from django.contrib.auth.models import User




class category(models.Model):
    name = models.CharField(max_length=100)



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=100)
    stock = models.IntegerField(max_length=100)
    image = models.ImageField()
    