# from django.shortcuts import render
# from .models import Signup
# def user_list(request):
# 	surya="surya"
# 	return render(request, 'tweet/tweet.html', {"resp":surya})
# def log_in(request):
# 	surya="surya"
# 	return render(request, 'tweet/login.html', {"resp":surya})
# def home_list(request):
# 	surya="surya"
# 	return render(request, 'tweet/home.html', {"resp":surya})
# # def signup(request):
#     if request.method == "GET":
#     	return render(request, 'tweet/home.html')
#     if request.method == "POST":
#     	form =SignupForm(data = request.POST)
#     	if form.is_valid():
#             user = form.save(False)
#             user.set_password(user.password)
#             user.save()
#             user = authenticate(username=user.username, password=request.POST['password'])
#             login(request, user)

#             return redirect('tweet/home.html')	




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



	

# Create your views here.
