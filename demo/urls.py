from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index),
    path('')
]

#localhost:8000/demo/home