from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Customer, Cart, CartItem, Order





def product_list(request):
    products = Product