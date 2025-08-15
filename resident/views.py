from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

# Create your views here.


def get_expiry_time() :
    return timezone.now() + timedelta(hours=10)
