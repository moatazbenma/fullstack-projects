from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('api/data/', views.intern_api, name='api-data'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_view, name='signup'),

]
