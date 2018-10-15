from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import login, authenticate
# from django.models import
# Create your views here.
def start(request):
	return render(request, 'twt/start.html',{})
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            raw_password = form.cleaned_data.get('confirmpassword')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
        return render(request, 'twt/login.html', {})
    else:
        form = UserForm()
    return render(request, 'twt/signup.html', {'form': form})

def home(request):
	return render(request, 'twt/home.html',{})

def logout(request):
	return render(request, 'twt/logout.html',{})

def login(request,user):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=username1, password=password1)
			login(request, user)
		return render(request, 'twt/home.html', {})
	else:
		form = LoginForm()
	return render(request, 'twt/login.html',{})