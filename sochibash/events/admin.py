from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Event, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = 'news'
    model = Gallery


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]
