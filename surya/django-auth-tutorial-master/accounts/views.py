from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import TweetForm
from .models import Tweet,Follow
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .forms import SignUpForm,ProfileForm
from .models import User
from django.contrib.auth import authenticate,login
from .models import Profile
from datetime import datetime
# from django.utils.encoding import force_text
# from django.utils.http import urlsafe_base64_decode
# from mysite.core.tokens import account_activation_token



# import ipdb



# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     form = SignUpForm(request.POST)
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def home(request):
    # twt = Tweets.objects.all()
    followers=Follow.objects.filter(following=request.user).count()
    following=Follow.objects.filter(followers=request.user).count()
    tweetscount=Tweets.objects.filter(user=request.user).count()
    if request.method == "POST":
        form = TweetForm(request.POST,request.FILES)
        # followers=Follow.objects.filter(following=request.user).count()
        # following=Follow.objects.filter(followers=request.user).count()
        # tweetscount=Tweets.objects.filter(user=request.user).count()

        if form.is_valid():
            tweets = form.save(commit=False)
            tweets.profile_image = form.cleaned_data['profile_image']
            tweets.user=request.user
            tweets.created_at = timezone.now()
            # upload(request.FILES['profile_image'])

            tweets.save()
        twt = Tweets.objects.all().order_by('-created_at')  
        return render(request, 'home.html', {'form': form, 'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount})  
    else:
        if request.user.is_active:
            twt = Tweets.objects.all().order_by('-created_at')
            form=TweetForm()
            return render(request, 'home.html', {'form': form, 'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount})
        else:
            return render(request, 'start.html')   
    return render(request, 'home.html', {'form': form})
    
# def home(request):
#     followers=Follow.objects.filter(following=request.user).count()
#     following=Follow.objects.filter(followers=request.user).count()
#     tweetscount=Tweets.objects.filter(user=request.user).count()
#     if request.method == "POST":
#         form = TweetForm(request.POST)
#         if form.is_valid():
#             tweet = form.save(commit=False)
#             tweet.user=request.user
            
#             tweet.published_date = timezone.now()
#             twt = Tweet.objects.all().order_by('-published_date')
#             tweet.save()
#             return render(request, 'home.html', {'form': form, 'twt1':twt})  
#     else:
#         if request.user.is_active:
#             twt = Tweet.objects.all().order_by('-published_date')
#             form=TweetForm()
#             return render(request, 'home.html', {'form': form, 'twt1':twt})
#         else:
#             return render(request, 'start.html')   
#     return render(request, 'home.html', {'form': form})	
def profile(request, pk):
    profile= get_object_or_404(User, pk=pk)
    pic=Profile.objects.filter(user=profile.id)
    twt=Tweet.objects.filter(user=profile.id)
    return render(request,'profile.html',{'profile':profile,'twt1':twt,'pic':pic}) 
def updateprofile(request):
    pic=Profile.objects.filter(user=request.user)
    twt=Tweet.objects.filter(user=request.user)
    p = request.user.profile
    if request.method == "POST":

        # pic=Profile.objects.filter(user=request.user)
        # twt=Tweet.objects.filter(user=request.user)
        # p = request.user.profile
        form = ProfileForm(request.POST,request.FILES, instance=p)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.profile_image = form.cleaned_data['profile_image']
            profile.header_image = form.cleaned_data['header_image']
            profile.save()

            #import ipdb
            #ipdb.set_trace()
            # profile = form.save(commit=False)
            # profile.birth_date = datetime.now
            
            # profile.profile_image = form.cleaned_data['profile_image']
            # profile.header_image = form.cleaned_data['header_image']
            # import ipdb
            # ipdb.set_trace()

           
            #profile = form.save(commit=False)
            #profile.user=request.user
            #profile.published_date = timezone.now()
            #profile.save()
        return render(request, 'updateprofile.html', {'form': form,'pic':pic,'twt1':twt})  
    else:
        # pic=Profile.objects.filter(user=request.user)
        # twt=Tweet.objects.filter(user=request.user)
        # p = request.user.profile
        form =ProfileForm(instance=p)
    
    return render(request, 'updateprofile.html', {'form': form,'pic':pic,'twt1':twt})
# def new_profile(request):
#     if request.method == "POST":
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.published_date = timezone.now()
#             profile.save()
#             return redirect('updateprofile')
#     else:
#         form = ProfileForm()
#     return render(request, 'updateprofile.html', {'form': form})
 #import ipdb
            #ipdb.set_trace()
            # profile = form.save(commit=False)
            # profile.birth_date = datetime.now
            
            # profile.profile_image = form.cleaned_data['profile_image']
            # profile.header_image = form.cleaned_data['header_image']
            # import ipdb
            # ipdb.set_trace()

           
            #profile = form.save(commit=False)
            #profile.user=request.user
            #profile.published_date = timezone.now()
            #profile.save()         