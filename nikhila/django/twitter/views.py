from django.shortcuts import render
from .forms import UserForm,LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Signup
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

# Create your views here.
def start(request):
	return render(request, 'twt/start.html',{})
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form1 = LoginForm(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # email = request.POST.get('password', '')
        # password = request.POST.get('password', '')
        if(Signup.objects.filter(username=username)):
            return render(request, 'twt/signup.html', {'form': form,'msg': 'username already exists'})
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            raw_password = form.cleaned_data.get('confirmpassword')
            # user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
        return render(request, 'twt/login.html', {'form': form1})
    else:
        form = UserForm()
    return render(request, 'twt/signup.html', {'form': form})

def home(request):
    user=Signup.objects.all()
    return render(request, 'twt/home.html', {'users':user})

def logout(request):
	return render(request, 'twt/logout.html',{})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        #user1 = authenticate(username = username, password = password)
        userdata = Signup.objects.filter(username=username).filter(password=password)
        user = Signup.objects.filter(username=username).filter(password=password).count()
        #login(request, user)
        if user==1:
            return render(request, 'twt/home.html', {'user':userdata})
        else:
            return render(request, 'twt/login.html', {'msg':'invalid username and password','form': form})   
    else:
        form = LoginForm()
    return render(request, 'twt/login.html', {'form': form})

# def login(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username = username, password = password)      

#     if user is not None:
#         auth.login(request, user)
#         return HttpResponseRedirect(reverse('home'))
#     else:
#         return HttpResponseRedirect('/accounts/invalid')