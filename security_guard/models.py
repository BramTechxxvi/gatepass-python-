from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class SecurityGuard(User):
    first_name = models.CharField(blank=False, null=False)
    last_name = models.CharField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    is_security_guard = models.BooleanField(default=False)
