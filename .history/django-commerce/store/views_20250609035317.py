from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Customer, Cart, CartItem, Order





def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'product': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_detail', {'product': product})



def cart_view(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)

        items = Cart
