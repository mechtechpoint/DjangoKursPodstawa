from django.urls import path, include
from . import views

app_name = 'baza'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name ='register'),
]