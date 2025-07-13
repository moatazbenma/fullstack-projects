from django.urls import path
from . import views
from .views import product_detail, product_list



urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail')
    path()
]
