# Generated by Django 4.1.7 on 2023-04-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdministratorMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('job_title', models.CharField(max_length=100, verbose_name='Должность')),
                ('image', models.ImageField(blank=True, upload_to='administrations/', verbose_name='Изображение')),
                ('bio', models.TextField(verbose_name='Краткая биография')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники администрации',
                'ordering': ('-fio',),
            },
        ),
    ]
