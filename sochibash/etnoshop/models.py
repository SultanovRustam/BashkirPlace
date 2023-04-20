from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name_plural = 'категории'
        verbose_name = 'категория'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='название')
    description = models.TextField(blank=True,
                                   verbose_name='описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='категория')
    image = models.ImageField(upload_to='product_images/',
                              verbose_name='изображение')

    class Meta:
        verbose_name_plural = 'товары'
        verbose_name = 'товар'

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='товар')
    author = models.CharField(max_length=255, verbose_name='автор')
    text = models.TextField(verbose_name='текст отзыва')
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        verbose_name='рейтинг')

    class Meta:
        verbose_name_plural = 'отзывы'
        verbose_name = 'отзыв'

    def __str__(self):
        return f'{self.product.name} - {self.rating}'
