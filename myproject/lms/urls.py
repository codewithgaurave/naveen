from django.contrib import admin
from django.urls import path
from lms import views

urlpatterns = [
    path('',views.index, name='home'),
]