from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    description = models.TextField("Описание занятия", blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name='Автор')
    event_date = models.DateTimeField(verbose_name="Время мероприятия")
    iframe_code = models.TextField(verbose_name='Код для вставки видео',
                                   blank=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title[:30]


class Gallery(models.Model):
    image = models.ImageField(verbose_name='Изображение',
                              upload_to='event_gallery')
    news = models.ForeignKey(Event, on_delete=models.CASCADE,
                             related_name='images')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
