from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import AdministratorMember


@admin.register(AdministratorMember)
class AdministratorMember(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = ("fio", "job_title", "preview")

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height: 288px; width:280px">')
