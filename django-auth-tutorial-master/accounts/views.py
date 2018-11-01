from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import TweetForm
from .models import Tweet
from django.shortcuts import render,redirect
from django.utils import timezone


# import ipdb



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def home(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user=request.user
            
            tweet.published_date = timezone.now()
            twt = Tweet.objects.all()
            tweet.save()

            return render(request, 'home.html', {'form': form, 'twt1':twt})
    else:
       	form=TweetForm()
    return render(request, 'home.html', {'form': form})	  
	
  
