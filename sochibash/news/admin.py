from django.contrib import admin
from django.utils.html import format_html

from .models import Gallery, News


class GalleryInline(admin.StackedInline):
    fk_name = 'news'
    model = Gallery


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["preview", "title", "author", "text"]
    inlines = [GalleryInline, ]

    def preview(self, obj):
        images = obj.images.all()[:3]

        if images:
            return format_html(
                ''.join(['<img src="{}" width="100"/>'.format(
                    image.image.url) for image in images]))

        return '-'

    preview.short_description = 'Превью изображений'
