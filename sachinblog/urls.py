from django.contrib import admin
from django.urls import path,include
from sachinblog import views

urlpatterns = [
    path('',views.home , name="home"),
    path('login',views.loginUser , name="login"),
    path('logout',views.logoutuser , name="logout")
]