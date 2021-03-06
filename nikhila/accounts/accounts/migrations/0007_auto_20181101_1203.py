# Generated by Django 2.0.9 on 2018-11-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181031_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='follow',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tweets',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]
