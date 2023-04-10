# Generated by Django 4.1.7 on 2023-04-08 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='activity',
            field=models.CharField(max_length=200, verbose_name='Дейтельность'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='children',
            field=models.CharField(max_length=100, verbose_name='Дети'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='family_status',
            field=models.CharField(max_length=100, verbose_name='Семейный статус'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fio',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.CharField(max_length=100, verbose_name='Национальность'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]
