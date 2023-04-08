from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AdministratorMember(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    job_title = models.CharField(max_length=100, verbose_name='Должность')
    image = models.ImageField(
        'Изображение',
        upload_to='administrations/',
        blank=True
    )

    class Meta:
        ordering = ('-fio',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники администрации'

    def __str__(self):
        return self.fio[:50]
