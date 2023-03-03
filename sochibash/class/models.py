from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Class(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    description=models.TextField("Описание занятия")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='classes')
    event_date = models.DateTimeField()
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
