from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Signup
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.
def start(request):
    return render(request, 'tweet/start.html',{})
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # form1 = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            raw_password = form.cleaned_data.get('confirmpassword')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home')
        # else:
        #     form = UserForm()
        #     return render(request, 'tweet/signup.html',{'form':form})
    else:
        form = UserForm()
    return render(request, 'tweet/signup.html', {'form': form})
# def signup(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  
#             user.save()
#             username = form.POST.get('username')
#             password = form.POST.get('password')
#             email = request.POST.get('email', '')
#             user = authenticate(username=username, password=password)
            
#             login(request, user)
#             return redirect('home')
        
#     else:
#         form = UserForm()
#     return render(request, 'tweet/signup.html', {'form': form})
def user_log(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            import ipdb
            ipdb.set_trace()    
            return HttpResponseRedirect('/home')
        else:
            form = LoginForm()
            import ipdb
            ipdb.set_trace() 
        return render(request, 'tweet/login.html', {'form':form})
            
        # import ipdb
        # ipdb.set_trace()

        # if user:
        #     if user.is_active:
        #         login(request, user)
        #         return HttpResponseRedirect('tweet/home.html')
        #     else:
        #         return HttpResponse('Your tweet account is disabled!')
        # else:
            
        #     return HttpResponse("Invalid login details supplied!")
    else:
        #import ipdb
        #ipdb.set_trace()
        if request.user.is_active:
            return HttpResponseRedirect('/home')
        else:
            form = LoginForm()

    return render(request, 'tweet/login.html', {'form':form})

def home(request):
    return render(request, 'tweet/home.html',{})
def user_logout(request):
    logout(request)
    #import ipdb
    #ipdb.set_trace()
    return redirect('start')


# def logout(request):
#     return render(request, 'tweet/logout.html',{})
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('tweet/home.html')
#             else:
#                 return HttpResponse('Your tweet account is disabled!')
#         else:
#             print("Invalid login details: {0}, {1}".format(username, password))
#             return HttpResponse("Invalid login details supplied!")
#     else:
#         return render(request, 'tweet/login.html', {})      


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         userdata = Signup.objects.filter(username=username).filter(password=password)
#         user = Signup.objects.filter(username=username).filter(password=password).count()
#         #login(request, user)
#         if user==1:
#             return render(request, 'tweet/home.html', {'user':userdata})
#         else:
#             return render(request, 'tweet/login.html', {'msg':'invalid username and password','form': form})   
#     else:
#         form = LoginForm()
#     return render(request, 'tweet/login.html', {'form': form})
    
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