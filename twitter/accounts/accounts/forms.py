from django import forms
from .models import Tweets,Profile
from .models import Follow,comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
        
class TweetForm(forms.ModelForm):


    class Meta:
        model = Tweets
        fields = ('text','profile_image',)


class SignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length=30,)
    # email = forms.EmailField( widget=forms.EmailInput(attrs={'size': 10,}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'size':90,}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','birth_date','location','profile_image','header_image',)
                  

class commentForm(forms.ModelForm):

    class Meta:
        model = comment
        fields = ('text','image',)


