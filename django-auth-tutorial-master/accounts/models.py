from django.db import models
from django.contrib.auth.models import User
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userprofile')
    text = models.TextField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='post_image', blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)

# Create your models here.
