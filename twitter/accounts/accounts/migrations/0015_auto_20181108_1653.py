# Generated by Django 2.1.2 on 2018-11-08 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0014_auto_20181108_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='likes',
        ),
        migrations.AddField(
            model_name='likes',
            name='like_id',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='like_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
