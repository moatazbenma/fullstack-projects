from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name="home"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-confirmation', views.order_confirmation, name='order_confirmation'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('decrease-quantity/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),
    path('profile/', views.profile_update, name='profile_update'),
]
