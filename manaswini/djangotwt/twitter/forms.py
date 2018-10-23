from django import forms

from .models import Signup

class UserForm(forms.ModelForm):
	confirmpassword = forms.CharField(widget=forms.PasswordInput())
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Signup
		fields = ('username', 'phoneNumber','email','password','confirmpassword')
		labels = {
        "username": "User Name",
    	}


class LoginForm(forms.ModelForm):
	
	class Meta:
		model = Signup
		fields = ('username','password',)