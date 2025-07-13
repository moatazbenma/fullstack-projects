from django.db import models
from django.db import 
from django.contrib.auth.models import User




class category(models.Model):
    name = models.CharField(max_length=100)



class Product(models.Model):
    