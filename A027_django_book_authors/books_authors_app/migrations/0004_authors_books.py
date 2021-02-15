# Generated by Django 2.2 on 2021-02-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_authors_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='books',
            field=models.ManyToManyField(related_name='author', to='books_authors_app.Books'),
        ),
    ]