from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Class


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = ("preview", "title", "author", "description", "event_date")

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    preview.short_description = "Изображение"
