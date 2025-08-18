from django.contrib.auth.models import AbstractUser
from django.db import models
from .utility import generate_code


# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    is_resident = models.BooleanField(default=False)
    is_security_guard = models.BooleanField(default=False)


class House(models.Model):
    house_number = models.PositiveIntegerField(blank=False, null=False)
    apartment_number = models.PositiveIntegerField(blank=False, null=False)
    street_name = models.CharField(max_length= 255, blank=False, null=False)
    resident = models.ForeignKey(User, on_delete=models.PROTECT)


class Invite(models.Model):
    code = models.CharField(max_length=6, default=generate_code(), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=False, blank=False)
    status = models.BooleanField(default=True)
    house = models.ForeignKey(House, on_delete=models.PROTECT)


class Visitor(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=255)
    last_name = models.CharField(blank=False, null=False, max_length=255)
    phone = models.CharField(blank=False, null=False, max_length=11, unique=True)
    invite = models.ForeignKey(Invite, on_delete=models.PROTECT)
