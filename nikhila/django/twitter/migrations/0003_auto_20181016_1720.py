# Generated by Django 2.0.9 on 2018-10-16 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20181016_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='following',
        ),
    ]