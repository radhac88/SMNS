from django import forms

from .models import Signup

class UserForm(forms.ModelForm):
	confirmpassword = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Signup
		fields = ('username', 'phonenumber','email','password','confirmpassword',)


