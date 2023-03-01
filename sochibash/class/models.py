from django.db import models


class Class(models.Model):
    title = models.TextField()
    author = models.TextField()
    event_date = models.DateTimeField()
    pub_date = models.DateTimeField(auto_now_add=True)

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
