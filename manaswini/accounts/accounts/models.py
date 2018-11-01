from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Tweets(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile',)
    # user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='User', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User', default='None')
    text = models.CharField(max_length=160,default=None)
    created_at = models.DateTimeField(default=timezone.now,null=True)
    profile_image = models.ImageField(upload_to='static/img', null=True, blank=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)
class Follow(models.Model):
    followers = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE,)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE,)
    status = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('followers', 'following')
