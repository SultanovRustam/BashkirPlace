# Generated by Django 2.2.6 on 2022-04-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0007_auto_20220405_1234"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="text",
            field=models.TextField(
                help_text="Введите текст поста", verbose_name="Текст поста"
            ),
        ),
    ]
