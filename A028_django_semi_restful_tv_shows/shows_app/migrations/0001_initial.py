# Generated by Django 2.2 on 2021-02-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('network', models.CharField(max_length=45)),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]
