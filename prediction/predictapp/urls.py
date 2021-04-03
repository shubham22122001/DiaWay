from django.contrib import admin
from django.urls import path
from predictapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('form',views.form,name='form'),
    path('result',views.result,name='result'),  
    path('about',views.about,name='about'),

]
