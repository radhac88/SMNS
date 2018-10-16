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
    return render(request, 'tweet/start.html',{})
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
        return render(request, 'tweet/login.html', {})
    else:
        form = UserForm()
    return render(request, 'tweet/signup.html', {'form': form})

def home(request):
    return render(request, 'tweet/home.html',{})

def logout(request):
    return render(request, 'tweet/logout.html',{})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        userdata = Signup.objects.filter(username=username).filter(password=password)
        user = Signup.objects.filter(username=username).filter(password=password).count()
        #login(request, user)
        if user==1:
            return render(request, 'tweet/home.html', {'user':userdata})
        else:
            return render(request, 'tweet/login.html', {'msg':'invalid username and password','form': form})   
    else:
        form = LoginForm()
    return render(request, 'tweet/login.html', {'form': form})
    
# def search(request):
#     if 'query' in request.GET and request.GET['query']:
#         search = request.GET['query']
        
#         result = Signup.objects.filter(Q(username__icontains=search))
       
#         return render(request, 'tweet/login.html', {'username':result,'search':search})
#     else:
#         return render(request, 'blog/logout.html') 
def search(request):
    query = request.GET.get('q')
    results= Signup.objects.filter(Q(username__icontains=query))

    return render(request, 'tweet/login.html', {'results': results})   

# def login(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username = username, password = password)      

#     if user is not None:
#         auth.login(request, user)
#         return HttpResponseRedirect(reverse('home'))
#     else:
#         return HttpResponseRedirect('/accounts/invalid')