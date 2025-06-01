from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.task_list, name='task-list'),
    path('add/', views.task_create, name='task-create'),
    path('edit/<int:pk>/', views.task_edit, name='task-edit'),
    path('delete/<int:pk>/', views.task_delete, name='task-delete'),
    path('about/', views.about_us, name="about_us"),
] 
