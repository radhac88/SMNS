from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Signup(models.Model):
    username = models.CharField(max_length=30, null=True)
    phonenumber=models.CharField(max_length=10,default=None, unique=True)
    email = models.EmailField(max_length=254, unique=True, db_index=True, primary_key=True, default=None)
    password = models.CharField(max_length=15, default=None)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.username

# Create your models here.

