from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Customer, Cart, CartItem, Order



def home(request):
    return render(request, 'store/base.html')


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'store/product_detail.html', {'product': product})


@login_required
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
    

@login_required
def add_to_cart(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=pk)
        cart, created = Cart.objects.get_or_create(user=request.user)
        item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            item.quantity += 1
            item.save()

        return redirect('cart_view')
    
    else:
        return redirect('login')

@login_required
def remove_from_cart(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=pk)
        item.delete()



        return redirect('cart_view')
    else:
        return redirect('login')
    
@login_required
def checkout_view(request):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.product.price * item.quantity for item in items)

        if request.method == 'POST':
            shipping_adress = request.POST.get('address', '')

            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                shipping_adress=shipping_adress,
            )

            items.delete()

            return redirect('order_confirmation')

        return render(request, 'store/checkout.html', {
            'items': items,
            'total_price': total_price
        })

    else:
        return redirect('login')
    


@login_required
def order_confirmation(request):
    return render(request, 'store/order_confirmation.html')





###################################################################

def 