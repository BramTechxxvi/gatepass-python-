from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class Admin(BaseUserAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'password']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2"),
            },
        ),
    )

