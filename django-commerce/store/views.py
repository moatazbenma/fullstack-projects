from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Customer, Cart, CartItem, Order, OrderItem
from .forms import RegisterForm, UserUpdateForm


@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'store/base.html')
    else:
        return redirect('login')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

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
    if request.method == 'POST':  # check POST first
        product = get_object_or_404(Product, id=pk)
        cart, created = Cart.objects.get_or_create(user=request.user)

        selected_color = request.POST.get('color')
        selected_size = request.POST.get('size')

        item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            color=selected_color,
            size=selected_size
        )

        if not item_created:
            item.quantity += 1
            item.save()

        return redirect(request.META.get('HTTP_REFERER', 'home'))

    return redirect('product_list')  # fallback if not POST




@login_required
def decrease_quantity(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()  # If quantity hits 0, remove from cart
        return redirect('cart')  # Change to 'cart_view' if your cart URL is named that




@login_required
def remove_from_cart(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=pk)
        item.delete()

        return redirect('cart')

    else:
        return redirect('login')
    









@login_required
def checkout_view(request):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.product.price * item.quantity for item in items)

        if request.method == 'POST':
            shipping_address = request.POST.get('address', '')

            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                shipping_address=shipping_address,
            )

            for item in items:
                OrderItem.objects.create(  
                order=order,
                product=item.product,
                quantity=item.quantity,
                color=item.color,
                size=item.size,
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



def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'store/product_list.html', {'category': category})



def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {  'category': category, 'products': products, 'categories':categories  })


###################################################################

def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
        
    else:
        form = RegisterForm()
    return render(request, 'store/signup.html', {'form': form})
    


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
        

    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')




@login_required
def profile_update(request):
    if request.method == 'POST':
        user_from = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_from.is_valid() and password_form.is_valid():
            user_from.save()
            user = password_form.save()
            update_session_auth_hash(request, user)
            return redirect('profile_update')
    
    else:
        user_from = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'store/profile_update.html', {
        'user_form': user_from,
        'password_form': password_form,
    })