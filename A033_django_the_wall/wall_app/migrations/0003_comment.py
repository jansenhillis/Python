# Generated by Django 2.2 on 2021-02-20 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('wall_app', '0002_auto_20210220_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall_app.Message')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='login_app.User')),
            ],
        ),
    ]
