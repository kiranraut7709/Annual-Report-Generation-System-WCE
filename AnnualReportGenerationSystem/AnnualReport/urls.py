"""AnnualReport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views, settings

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name="Home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('ourTeam', views.ourTeam, name="ourTeam"),
    path('adminApp', include('AdminApp.urls')),
    path('CSE', include('CSE.urls')),
    path('IT', include('IT.urls')),
    path('Civil', include('Civil.urls')),
    path('ME', include('ME.urls')),
    path('Electrical', include('Electrical.urls')),
    path('Electronics', include('Electronics.urls')),
    path('admin/', admin.site.urls),

    
]
