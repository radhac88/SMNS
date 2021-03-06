from django import forms
from .models import Tweets,Profile
from .models import Follow,comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


        
class TweetForm(forms.ModelForm):
	

    class Meta:
        model = Tweets
        fields = ('text','profile_image',)
    # class Meta:
    # 	model = Follow
    # 	fields = ('profile_pic',)
    		



class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','birth_date','location','profile_image','header_image',)
                  



class commentForm(forms.ModelForm):

    class Meta:
        model = comment
        fields = ('text','image',)

