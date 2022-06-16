
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('signup',views.signup,name='signup'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('logoutpage',views.logoutpage,name='logoutpage'),
]
