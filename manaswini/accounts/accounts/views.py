from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Tweets,Follow
from .forms import TweetForm,SignUpForm
from django.utils import timezone
from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from django.contrib.auth import authenticate,login
from datetime import datetime


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            checkbox = form.cleaned_data.get('checkbox')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def start(request):
	return render(request, 'start.html',{})
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


def profile(request, pk):
	profile= get_object_or_404(User, pk=pk)
	user_id = request.POST.get('id')
	action = request.POST.get('action')
	if user_id and action:
		try:
			user = User.objects.get(id=user_id)
			if action == 'follow':
				Profile.objects.get_or_create(user_from=request.user,user_to=user)
			else:
				Profile.objects.filter(user_form=request.user,user_to=user).delete()
			return JsonResponse({'status':'ok'})
		except User.DoesNotExist:
			return JsonResponse({'status':'ok'})
	return render(request,'profile.html',{'profile':profile}) 	














# def new(request):
#     if request.method == "POST":
#         form = TweetForm(request.POST)
#         if form.is_valid():
#             tweet = form.save(commit=False)
#             tweet.user=request.user
#             tweet.published_date = timezone.now()
#             tweet.save()
#             return render(request, 'home.html', {'form': form})
#     else:
#        	form=TweetForm()
#     return render(request, 'home.html', {'form': form})
# def home(request):
# 	twt = Tweets.objects.all()

# 	followers=Follow.objects.filter(following=request.user).count()
# 	following=Follow.objects.filter(followers=request.user).count()
# 	tweetscount=Tweets.objects.filter(user=request.user).count()
# 	return render(request, 'home.html', {'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount})
