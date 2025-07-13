from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup_view, name='signup'),
    path()
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-confirmation', views.order_confirmation, name='order_confirmation'),
]
