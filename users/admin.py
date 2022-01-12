from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User


class UserAdmin(DefaultUserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff', 'code', 'address', 'city'
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'code')
        }),
    )


admin.site.register(User, UserAdmin)
