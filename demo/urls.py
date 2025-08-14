from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index),
    path('about', views.about),
    path('contact', views.contact),
]

#localhost:8000/demo/home