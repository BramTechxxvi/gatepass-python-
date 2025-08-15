from account.models import UserAccount
from django.db import models

# Create your models here.

class Resident(UserAccount):
    is_resident = models.BooleanField(default=False)


class House(models.Model):
    house_number = models.PositiveIntegerField(blank=False, null=False)
    apartment_number = models.PositiveIntegerField(blank=False, null=False)
    street_name = models.CharField(max_length= 255, blank=False, null=False)
    resident = models.ForeignKey(Resident, on_delete=models.PROTECT)


class Invite(models.Model):
    code = models.CharField(max_length=6, default='', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=False, blank=False)
    status = models.BooleanField(default=True)
    house = models.ForeignKey(House, on_delete=models.PROTECT)


class Visitor(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=255)
    last_name = models.CharField(blank=False, null=False, max_length=255)
    phone = models.CharField(blank=False, null=False, max_length=11)
    invite = models.ForeignKey(Invite, on_delete=models.PROTECT)
