from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.htmlfile, name='htmlfl'),
    path('home', views.htmlfile, name='home'),
    path('add_quotes', views.add_quotes, name='add_quotes'),
    #path('delete_quotes', views.delete_quotes, name='delete_quotes'),


]
