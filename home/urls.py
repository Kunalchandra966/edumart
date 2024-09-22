from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="index"),  
    path('home', views.home, name="home"),  
    path('login', views.loginuser, name="login") , 
    path('logout', views.logoutuser, name="logout"),
    path('register', views.registeruser, name="register")  
]