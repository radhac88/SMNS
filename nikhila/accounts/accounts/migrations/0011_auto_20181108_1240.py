# Generated by Django 2.0.9 on 2018-11-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(blank=True, default=None, max_length=160),
        ),
    ]
