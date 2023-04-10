from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    age = models.IntegerField(verbose_name='Возраст')
    nationality = models.CharField(max_length=100,
                                   verbose_name='Национальность')
    activity = models.CharField(max_length=200, verbose_name='Дейтельность')
    family_status = models.CharField(max_length=100,
                                     verbose_name='Семейный статус')
    children = models.CharField(max_length=100, verbose_name='Дети')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Автор'
    )
    image = models.ImageField(
        'Фото профиля',
        upload_to='meeting/profile/',
        blank=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.fio[:30]
