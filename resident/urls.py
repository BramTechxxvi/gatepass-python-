from django.contrib.auth.urls import path
from . import views

urlpatterns = [
    path('create', views.create_resident),
]
