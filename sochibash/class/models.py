from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Class(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    description = models.TextField("Описание занятия", blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='classes',
        verbose_name='Автор')
    event_date = models.DateTimeField(verbose_name="Время события")
    image = models.ImageField(
        'Картинка',
        upload_to='class/',
        blank=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

    def __str__(self):
        return self.title[:30]
