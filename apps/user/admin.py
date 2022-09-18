from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
                'name',
            )
        }),
    )
    list_display = (
        'id',
        'username',
        'name'
    )
