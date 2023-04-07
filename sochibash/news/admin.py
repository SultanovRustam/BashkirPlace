from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = ("title", "author", "text")

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')