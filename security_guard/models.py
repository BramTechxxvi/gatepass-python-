from account.models import UserAccount
from django.db import models

# Create your models here.

class SecurityGuard(UserAccount):
    # first_name = models.CharField(blank=False, null=False)
    # last_name = models.CharField(blank=False, null=False)
    # email = models.EmailField(blank=False, null=False, unique=True)
    is_security_guard = models.BooleanField(default=False)
