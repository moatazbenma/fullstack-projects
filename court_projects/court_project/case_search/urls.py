from django.urls import path
from . import views

app_name = 'case_search'  

urlpatterns = [
    path('', views.search_form, name='search_form'),      
    path('results/', views.search_view, name='search'),         
]