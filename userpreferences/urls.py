
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('preferences',views.preferences,name='preferences'),
]
