from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('edit-page/', edit_page, name='edit_page')
]