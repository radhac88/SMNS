from django.contrib import admin
# Register your models here.
from .models import Tweets,Profile
admin.site.register(Tweets)
from .models import Follow
admin.site.register(Follow)
admin.site.register(Profile)
