"""Projekt1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Sklep.views import *
from baza.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('produkty', produkty, name='produkty'),
    path('produkt/<id>', produkt, name='produkt'),
    path('dodajkoszyk/<id>', dodajkoszyk, name='dodajkoszyk'),
    path('koszyk', koszyk, name='koszyk'),
    path('kosz/<id1>/<id2>', kosz, name='kosz'),
    path('wyslij', wyslij, name='wyslij'),
    path('baza/', include('baza.urls')),
]


