from django.shortcuts import render
from .forms import UserForm,LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Signup
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import View


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
            #login(request, user)
        return render(request, 'twt/login.html', {})
    else:
        form = UserForm()
    return render(request, 'twt/signup.html', {'form': form})

def home(request):
	return render(request, 'twt/home.html',{})

def logout(request):
	return render(request, 'twt/logout.html',{})
def user_log(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        # import ipdb
        # ipdb.set_trace()

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('twt/home.html')
            else:
                return HttpResponse('Your tweet account is disabled!')
        else:
            
            return HttpResponse("Invalid login details supplied!")
    else:
        form = LoginForm()

    return render(request, 'twt/login.html', {'form':form})
def follow(request,event_id):
    user = request.user
    event = Event.objects.get(id=event_id)

    event.users.add(user)
    event.save()