from django.contrib import admin

from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'end_time', 'title')
    exclude = ['iso_start', 'iso_end']


admin.site.register(Schedule, ScheduleAdmin)
