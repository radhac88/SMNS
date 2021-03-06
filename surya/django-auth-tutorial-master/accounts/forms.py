from django import forms

from .models import Tweet,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Follow


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

        
class TweetForm(forms.ModelForm):
	

    class Meta:
        model = Tweet
        fields = ('text','profile_image',)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','birth_date','location','profile_image','header_image',)
                  

