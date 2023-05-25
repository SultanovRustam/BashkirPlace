# Generated by Django 4.1.7 on 2023-05-18 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.AddField(
            model_name='event',
            name='iframe_code',
            field=models.TextField(default='', verbose_name='Код для вставки видео'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='event_gallery', verbose_name='Изображение')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.event')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
