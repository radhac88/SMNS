from django.contrib import admin
from .models import Signup,follow
from .forms import UserForm

admin.site.register(Signup)

admin.site.register(follow)
# Register your models here.
