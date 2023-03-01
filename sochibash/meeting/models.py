from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    fio = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    activity = models.CharField(max_length=200)
    family_status = models.CharField(max_length=100)
    children = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
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
