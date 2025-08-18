from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, House


# Register your models here.

@admin.register(User)
class Admin(BaseUserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone', 'password', 'is_resident', 'is_security_guard', "is_superuser"]
    list_editable = ['first_name', 'last_name', 'is_resident', 'is_security_guard', 'is_superuser']

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "first_name", "last_name", "email", "phone", "password"),
            },
        ),
    )

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['house_number', 'apartment_number', 'street_name']