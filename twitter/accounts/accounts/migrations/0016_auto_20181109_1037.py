# Generated by Django 2.1.2 on 2018-11-09 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20181108_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='like_id',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='like_id', to='accounts.Tweets'),
        ),
    ]
