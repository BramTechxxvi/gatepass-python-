from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resident(User):
    first_name = models.CharField(blank=False, null=False)
    last_name = models.CharField(blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(unique=True, blank=False, null=False)
    is_resident = models.BooleanField(default=False)

class House(models.Model):
    house_number = models.PositiveIntegerField(blank=False, null=False)
    apartment_number = models.PositiveIntegerField(blank=False, null=False)
    street_name = models.CharField(max_length= 255, blank=False, null=False)
    resident = models.ForeignKey(Resident, on_delete=models.PROTECT)

