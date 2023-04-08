from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import AdministratorMember


@admin.register(AdministratorMember)
class AdministratorMember(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = ("preview", "fio", "job_title")

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px">')

    preview.short_description = "Изображение"
