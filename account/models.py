from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserAccount(AbstractUser):
    first_name = models.CharField(blank=False, null=False)
    last_name = models.CharField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    phone = models.CharField(blank=False, null=False, max_length=11, unique=True)
