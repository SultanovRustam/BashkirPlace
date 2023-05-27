from django.contrib import admin
from django.utils.html import format_html

from .models import Event, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = 'news'
    model = Gallery


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["preview", "title", "author", "description", "event_date"]
    inlines = [GalleryInline, ]

    def preview(self, obj):
        images = obj.images.all()[:3]

        if images:
            return format_html(
                ''.join(['<img src="{}" width="200" height="250"/>'.format(
                    image.image.url) for image in images]))
        else:
            return '-'

    preview.short_description = 'Превью изображений'
