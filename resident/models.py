from django.db import models

# Create your models here.

class Resident(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=11, blank=False, null=False)
    password = models.CharField(max_length=16, blank=False, null=False)
