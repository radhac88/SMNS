from django.shortcuts import render
# Create your views here.
def start(request):
	return render(request, 'twt/start.html',{})
def signup(request):
	return render(request, 'twt/signup.html',{})
def home(request):
	return render(request, 'twt/home.html',{})
def login(request):
	return render(request, 'twt/login.html',{})