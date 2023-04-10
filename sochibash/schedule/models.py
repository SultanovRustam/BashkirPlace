import datetime

from django.db import models


class Schedule(models.Model):
    date = models.DateField(verbose_name='Дата')
    start_time = models.TimeField(verbose_name='Начало')
    end_time = models.TimeField(verbose_name='Окончание')
    title = models.CharField(verbose_name='Название', max_length=200)
    description = models.TextField('Описание')
    iso_start = models.CharField(max_length=100, blank=True, null=True)
    iso_end = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        dt_start = datetime.datetime.combine(self.date, self.start_time)
        dt_end = datetime.datetime.combine(self.date, self.end_time)
        self.iso_start = dt_start.isoformat()
        self.iso_end = dt_end.isoformat()
        super(Schedule, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Событие'
        verbose_name_plural = 'Событие'

    def __str__(self):
        return self.title[:30]
