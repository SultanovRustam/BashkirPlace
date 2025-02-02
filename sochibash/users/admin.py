from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'email',
    )
    ordering = ('email',)
    search_fields = ('email', 'last_name')
    list_filter = ('email', 'first_name', 'last_name')
