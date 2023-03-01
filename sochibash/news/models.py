from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class News(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField("Текст новости", help_text="Введите текст новости")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='news/',
        blank=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title[:30]
