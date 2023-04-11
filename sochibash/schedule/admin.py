from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = ('preview', 'date', 'start_time', 'end_time', 'title')
    exclude = ['iso_start', 'iso_end']

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="max-height: 200px;">')


admin.site.register(Schedule, ScheduleAdmin)
