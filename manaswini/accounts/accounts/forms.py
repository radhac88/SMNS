from django import forms

from .models import Tweets
from .models import Follow
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    checkbox = forms.BooleanField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'checkbox',)


        
class TweetForm(forms.ModelForm):
	

    class Meta:
        model = Tweets
        fields = ('text','profile_image',)
    # class Meta:
    # 	model = Follow
    # 	fields = ('profile_pic',)
    		














# from django import forms

# from .models import Tweets
# class TweetForm(forms.ModelForm):
	

#     class Meta:
#         model = Tweets
#         fields = ('text',)