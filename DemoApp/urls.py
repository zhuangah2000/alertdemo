from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home-page'),
    path('send/', views.send, name='test'),

]