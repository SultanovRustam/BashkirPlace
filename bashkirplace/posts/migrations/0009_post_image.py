# Generated by Django 2.2.16 on 2022-04-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0008_auto_20220405_1242"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="posts/", verbose_name="Картинка"
            ),
        ),
    ]
