# Generated by Django 2.0.9 on 2018-10-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181026_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]