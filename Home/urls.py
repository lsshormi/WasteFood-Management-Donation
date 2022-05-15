from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
   path("", views.home, name='home'),
   path("about/", views.about, name='about'),
   path("gallery/", views.gallery, name='gallery'),
   path("contact/", views.contact, name='contact'),
   path("Donate/", views.donate, name='Donate'),
   path("joinUs/", views.joinUs, name='joinUs'),
   path("login", views.loginUser, name='login'),
   path("logout", views.logoutUser, name='logout'),
   path("signup", views.signupUser, name='signup'),
   path("Admin/", views.Admin, name='Admin'),
]