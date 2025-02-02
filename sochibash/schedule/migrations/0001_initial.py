# Generated by Django 4.1.7 on 2023-04-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('start_time', models.TimeField(verbose_name='Начало')),
                ('end_time', models.TimeField(verbose_name='Окончание')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='schedule/', verbose_name='Картинка')),
                ('iso_start', models.CharField(blank=True, max_length=100, null=True)),
                ('iso_end', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'Событие',
                'ordering': ('-date',),
            },
        ),
    ]
