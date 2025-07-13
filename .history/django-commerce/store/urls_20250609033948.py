from django.urls import path
from . import views
from .views import product_detail, product_list



urlpatterns = [
    path('', views.home, name="home")
    path('products/<int:pk>/', view)
]
