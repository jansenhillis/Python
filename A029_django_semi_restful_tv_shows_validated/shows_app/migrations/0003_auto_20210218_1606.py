# Generated by Django 2.2 on 2021-02-19 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0002_auto_20210218_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
