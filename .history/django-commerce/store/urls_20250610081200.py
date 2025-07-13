from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add-tocart/<int:pk>/', views.add_to_cart, name='addtocart'),
    path('removefromcart/<int:pk>/', views.remove_from_cart, name='removefromcart'),
    path('checkout/', views.checkout_view, name='checkout'),
]
