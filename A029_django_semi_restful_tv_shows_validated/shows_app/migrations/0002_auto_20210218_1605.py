# Generated by Django 2.2 on 2021-02-19 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]