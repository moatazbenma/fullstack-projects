from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path('events', views.allevents, name="events"),
    path('login/', views.auth_login, name="login"),
    path('signup/', views.auth_signup, name="signup"),
    path('logout/', views.auth_logout, name="logout"),
    path('event_detail/<int:pk>/', views.event_detail, name="event_detail"),
    path('event_creation/', views.event_creation, name="event_creation"),
    path('registration/<int:pk>', views.registration, name="registration"),
    path('my_registrations/', views.registrationlist, name="my_registrations"),
    path('unregister/<int:pk>', views.deleteevent, name="unregister"),
    path('editprofile/', views.editprofile, name="editprofile")
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)