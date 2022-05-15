"""WasteFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from .views import *

from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "WasteFood Management & Donation Admin"
admin.site.site_title = "WasteFood Management Admin Portal"
admin.site.index_title = "Welcome to WasteFood Management & Donation"

# app_name = 'Home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
]