from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Tweets,Follow,Profile,comment
from .forms import TweetForm
from django.utils import timezone
from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from .forms import SignUpForm,ProfileForm,commentForm
from django.contrib.auth import authenticate,login


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
	pic=Profile.objects.filter(user=request.user)
	if request.method == "POST":
		form =TweetForm(request.POST,request.FILES)
		form1=commentForm(request.POST,request.FILES)
		if form.is_valid():
			tweet = form.save(commit=False)
			tweet.user=request.user
			tweet.profile_image = form.cleaned_data['profile_image']
			tweet.save()
			twt = Tweets.objects.all().order_by('-created_at')
			followers=Follow.objects.filter(following=request.user).count()
			following=Follow.objects.filter(followers=request.user).count()
			tweetscount=Tweets.objects.filter(user=request.user).count()
			return render(request, 'home.html', {'form': form, 'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount,'form1':form1,'pic':pic})  
		
	else:
		if request.user.is_active:
			twt = Tweets.objects.all().order_by('-created_at')
			followers=Follow.objects.filter(following=request.user).count()
			following=Follow.objects.filter(followers=request.user).count()
			tweetscount=Tweets.objects.filter(user=request.user).count()
			form=TweetForm()
			form1=commentForm(request.POST)
			return render(request, 'home.html', {'form': form, 'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount,'form1':form1,'pic':pic})
		else:
			return render(request, 'start.html')
	return render(request, 'home.html', {'form': form})	

def profile(request, pk):
    profile= get_object_or_404(User, pk=pk)
    pic=Profile.objects.filter(user=profile.id)
    twt=Tweets.objects.filter(user=profile.id)
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    user = User.objects.get(id=user_id)
    if user_id and action:
    	try:
    		user = User.objects.get(id=user_id)
    		if action == 'follow':
    			Follow.objects.get_or_create(followers=request.user,following=user)
    		else:
    			Follow.objects.filter(followers=request.user,following=user).delete()
    		return JsonResponse({'status':'ok'})
    	except User.DoesNotExist:
    		return JsonResponse({'status':'ok'})
    return render(request,'profile.html',{'profile':profile,'twt1':twt,'pic':pic,"action":action,'user':user}) 

def updateprofile(request):
    pic=Profile.objects.filter(user=request.user)
    twt=Tweets.objects.filter(user=request.user)
    try:
	    if request.method == "POST":
	        form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
	        if form.is_valid():
	            profile = form.save(commit=False)
	            profile.user=request.user
	            profile.profile_image = form.cleaned_data['profile_image']
	            profile.header_image = form.cleaned_data['header_image']
	            profile.save()
	        return render(request, 'updateprofile.html', {'form': form,'pic':pic,'twt1':twt})  
	    else:
	        form =ProfileForm(instance=request.user.profile)
	        return render(request, 'updateprofile.html', {'form': form,'pic':pic,'twt1':twt})  
    except:
    	form =ProfileForm(request.POST,request.FILES)
    	if form.is_valid():
            profile = form.save(commit=False)
            profile.user=request.user
            profile.profile_image = form.cleaned_data['profile_image']
            profile.header_image = form.cleaned_data['header_image']
            profile.save()
    	return render(request, 'updateprofile.html', {'form': form,'pic':pic,'twt1':twt})	
    return render(request, 'updateprofile.html', {'form': form,'pic':pic,'twt1':twt})

def comments(request, pk):
		post = get_object_or_404(Tweets, pk=pk)
		comments=comment.objects.filter(twtid=post.pk)
		return render(request, 'comments.html', {'post': post,'comment':comments})

def savecomment(request,pk):
	tweets = get_object_or_404(Tweets, pk=pk)
	if request.method == "POST":
			form1=commentForm(request.POST,request.FILES)
			if form1.is_valid():
					tweet = form1.save(commit=False)
					tweet.twtid=get_object_or_404(Tweets, pk=pk)
					tweet.image = form1.cleaned_data['image']
					tweet.save()
					# twt = Tweets.objects.all().order_by('-created_at')
					# followers=Follow.objects.filter(following=request.user).count()
					# following=Follow.objects.filter(followers=request.user).count()
					# tweetscount=Tweets.objects.filter(user=request.user).count()
					return redirect('home')