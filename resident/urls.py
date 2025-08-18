from django.contrib.auth.urls import path
from . import views

urlpatterns = [
    path('add+house', views.add_house),
    path('create', views.create_resident),
]
