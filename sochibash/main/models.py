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
    bio = models.TextField(verbose_name='Краткая биография')

    class Meta:
        ordering = ('-fio',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники администрации'

    def __str__(self):
        return self.fio[:50]


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    published = models.BooleanField(verbose_name='Опубликовано',
                                    default=False)

    def save(self, *args, **kwargs):
        if self.published:
            try:
                published_banner = Banner.objects.get(published=True)
                if self != published_banner:
                    published_banner.published = False
                    published_banner.save()
            except Banner.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Banner {self.id}"

    class Meta:
        verbose_name = 'Изображение для главной страницы'
        verbose_name_plural = 'Изображения для главной страницы'
