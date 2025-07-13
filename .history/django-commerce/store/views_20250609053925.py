from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Customer, Cart, CartItem, Order





def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'product': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'store/product_detail', {'product': product})



def cart_view(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)

        items = CartItem.objects.filter(cart=cart)

        total_price = sum(item.product.price * item.quantity for item in items)

        context = {
            'items': items,
            'total_price': total_price
        }

        return render(request, 'store/cart.html', context)
    
    else:
        return redirect('login')
    


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.id)
        item, item_created = CartItem.objects.filter(cart=cart, product=product)

        if not item_created:
            item
