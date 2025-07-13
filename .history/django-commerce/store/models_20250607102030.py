from django.db import models
from django.contrib.auth.models import User




class category(models.Model):
    name = models.CharField(max_length=100)



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to=)
    category = models.CharField(max_length=100)
    created_at = models.DateField(null=True, blank=True)