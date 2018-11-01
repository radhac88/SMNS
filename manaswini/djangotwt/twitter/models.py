from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Signup(models.Model):
    username = models.CharField(max_length=30, null=True)

   
    email = models.EmailField(max_length=254, unique=True, db_index=True, primary_key=True, default=None, blank=True)
    password = models.CharField(max_length=15, default=None, unique=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.username
class Tweet(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE, unique=True)
    text = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True) 



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.user
