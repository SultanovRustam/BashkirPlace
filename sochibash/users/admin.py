from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'first_name',
        'last_name',
        'email',
    )
    ordering = ('email',)
    search_fields = ('username', 'email', 'last_name')
    list_filter = ('username', 'email', 'first_name', 'last_name')
