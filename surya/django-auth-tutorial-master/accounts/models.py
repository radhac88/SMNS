from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.models import User
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userprofile')
    text = models.TextField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='static/images', blank=True, null=True)
    header_image = models.ImageField(upload_to='static/images', blank=True, null=True)
    

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)

   