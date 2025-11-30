from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Moderation', {'fields': ('is_moderator','warnings','suspension_until')}),
    )
    list_display = ('username','email','is_moderator','warnings','suspension_until','is_active')
