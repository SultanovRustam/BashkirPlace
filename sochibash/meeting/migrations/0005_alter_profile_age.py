# Generated by Django 4.1.7 on 2023-05-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.CharField(max_length=5, verbose_name='Возраст'),
        ),
    ]
