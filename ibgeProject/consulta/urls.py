from django.contrib import admin
from django.urls import path
from consulta import views

urlpatterns = [
    path("api/", views.home)
    
]