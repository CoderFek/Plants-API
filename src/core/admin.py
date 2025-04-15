from django.contrib import admin
from .models import Plant, CachePlant, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_active', 'is_staff', 'date_joined']  # Customize the fields you want to show
    search_fields = ['username', 'email']  # Add search fields
    ordering = ['date_joined']  # Add default ordering if needed

admin.site.register(CustomUser,CustomUserAdmin)

admin.site.register(Plant)
admin.site.register(CachePlant)
