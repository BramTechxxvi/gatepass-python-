from account.models import UserAccount
from django.db import models

# Create your models here.

class SecurityGuard(UserAccount):
    is_security_guard = models.BooleanField(default=False)
