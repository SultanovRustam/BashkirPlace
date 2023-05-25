from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Gallery, News


class GalleryInline(admin.TabularInline):
    fk_name = 'news'
    model = Gallery


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]

