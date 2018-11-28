from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Tweets,Follow,Profile,comment,Replycomment
from .forms import TweetForm,commentForm,replycommentForm
from django.utils import timezone
from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from .forms import SignUpForm,ProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Tweets,Follow,Profile
from .forms import TweetForm
from django.utils import timezone
from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from .forms import SignUpForm,ProfileForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect,HttpResponse
from django.http import JsonResponse




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
            Profile.objects.create(user=request.user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def home(request):
	if request.method == "POST":
		form = TweetForm(request.POST,request.FILES)
		
		form1 = commentForm(request.POST)
		form2=replycommentForm(request.POST)
		if form.is_valid():
			tweet = form.save(commit=False)
			tweet.user=request.user
			tweet.published_date = timezone.now()
			twt = Tweets.objects.all().order_by('-created_at')
			tweet.save()
			form = TweetForm()
			followers=Follow.objects.filter(following=request.user).count()
			following=Follow.objects.filter(followers=request.user).count()
			ran = Tweets.objects.all().order_by('?')[:5]
			tweetscount=Tweets.objects.filter(user=request.user).count()
			pic=Profile.objects.filter(user=request.user)
			commentslist=[]
			for i in twt:
				comments=comment.objects.filter(twtid=i.id)
				commentslist.append(comments)
			replycommentlist=[]	
			for i in twt:
				reply=Replycomment.objects.filter(replyid=i.id)	
				replycommentlist.append(reply)
			twtlist=zip(twt,commentslist,replycommentlist)
			return render(request, 'home.html', {'form': form, 'form2':form2 ,'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount,'form1':form1,'pic':pic,'random_users': ran,'twtlist':twtlist})  
	else:
		if request.user.is_active:
			twt = Tweets.objects.all().order_by('-created_at')
			followers=Follow.objects.filter(following=request.user).count()
			following=Follow.objects.filter(followers=request.user).count()
			tweetscount=Tweets.objects.filter(user=request.user).count()
			ran = Profile.objects.all().order_by('?')[:5]
			pic=Profile.objects.filter(user=request.user)
			form=TweetForm()
			form1 = commentForm(request.POST)
			form2=replycommentForm(request.POST)
			commentslist=[]
			for i in twt:
				comments=comment.objects.filter(twtid=i.id)
				commentslist.append(comments)
			replycommentlist=[]		
			for i in twt:
				reply=Replycomment.objects.filter(replyid=i.id)
				replycommentlist.append(reply)	
			twtlist=zip(twt,commentslist,replycommentlist)
			return render(request, 'home.html', {'form': form,'form2':form2, 'random_users': ran,'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount,'form1':form1,'pic':pic,'twtlist':twtlist})
		else:
			return render(request, 'start.html')
	return render(request, 'home.html', {'form': form,'random_users': ran,'pic':pic})	


def profile(request, pk):
	try:
		form =ProfileForm(instance=request.user.profile)
		profile= get_object_or_404(User, pk=pk)
		pic=Profile.objects.filter(user=profile.id)
		twt=Tweets.objects.filter(user=profile.id)
		followers=Follow.objects.filter(following=profile.id).count()
		following=Follow.objects.filter(followers=profile.id).count()
		tweetscount=Tweets.objects.filter(user=profile.id).count()
		form1 = commentForm(request.POST)
		if(request.user!= profile):
			status=Follow.objects.filter(followers=request.user,following=profile)
		else:
			status="ok"
		if request.is_ajax():
		    user_id = request.GET.get('id')
		    action = request.GET.get('action')
		    if action == "follow":
		        Follow.objects.get_or_create(followers=request.user,following=profile)
		        return JsonResponse({'status':'ok','data1':'follow'})
		    elif action == "unfollow":
		        Follow.objects.filter(followers=request.user,following=profile).delete()
		        return JsonResponse({'status':'ok','data1':'unfollow'})
		commentslist=[]
		for i in twt:
				comments=comment.objects.filter(twtid=i.id)
				commentslist.append(comments)
		replycommentlist=[]
		for i in twt:
				reply=Replycomment.objects.filter(replyid=i.id)
				replycommentlist.append(reply)	
		stwtlist=zip(twt,commentslist,replycommentlist)
		return render(request,'profile.html',{'profile':profile,'twt1':twt,'pic':pic,'twtlist':twtlist,'status':status,'form': form,'followers':followers,'following':following,'twtcount':tweetscount,'form1':form1,}) 
	except:
		form =ProfileForm()
		profile= get_object_or_404(User, pk=pk)
		pic=Profile.objects.filter(user=profile.id)
		twt=Tweets.objects.filter(user=profile.id)
		followers=Follow.objects.filter(following=profile.id).count()
		following=Follow.objects.filter(followers=profile.id).count()
		tweetscount=Tweets.objects.filter(user=profile.id).count()
		form1 = commentForm(request.POST)
		if(request.user!= profile):
			status=Follow.objects.filter(followers=request.user,following=profile)
		else:
			status="ok"
		if request.is_ajax():
		    user_id = request.GET.get('id')
		    action = request.GET.get('action')
		    if action == "follow":
		        Follow.objects.get_or_create(followers=request.user,following=profile)
		        return JsonResponse({'status':'ok','data1':'follow'})
		    elif action == "unfollow":
		        Follow.objects.filter(followers=request.user,following=profile).delete()
		        return JsonResponse({'status':'ok','data1':'unfollow'})
		commentslist=[]
		for i in twt:
				comments=comment.objects.filter(twtid=i.id)
				commentslist.append(comments)
		replycommentlist=[]		
		for i in twt:
				reply=Replycomment.objects.filter(replyid=i.id)
				replycommentlist.append(reply)	
		twtlist=zip(twt,commentslist,replycommentlist)        
		return render(request,'profile.html',{'profile':profile,'twt1':twt,'twtlist':twtlist,'pic':pic,'status':status,'form': form,'followers':followers,'following':following,'twtcount':tweetscount,'form1':form1,}) 

def updateprofile(request):
    pic=Profile.objects.filter(user=request.user)
    twt=Tweets.objects.filter(user=request.user)
    followers=Follow.objects.filter(following=request.user).count()
    following=Follow.objects.filter(followers=request.user).count()
    tweetscount=Tweets.objects.filter(user=request.user).count()
    form =ProfileForm(request.POST)
    try:
	    if request.method == "POST":
	        form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
	        if form.is_valid():
	            profile = form.save(commit=False)
	            profile.user=request.user
	            profile.profile_image = form.cleaned_data['profile_image']
	            profile.header_image = form.cleaned_data['header_image']
	            profile.save()
	        commentslist=[]
	        for i in twt:
	        	comments=comment.objects.filter(twtid=i.id)
	        	commentslist.append(comments)
	        replycommentlist=[]
	        for i in twt:
	        	reply=Replycomment.objects.filter(replyid=i.id)	
	        	replycommentlist.append(reply)
	        twtlist=zip(twt,commentslist,replycommentlist)
	        return render(request, 'updateprofile.html', {'form': form,'pic':pic,'twtlist':twtlist,'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount})
	    else:
	    		twt=Tweets.objects.filter(user=request.user)
	    		form =ProfileForm(instance=request.user.profile)
	    		commentslist=[]
	    		for i in twt:
	    			comments=comment.objects.filter(twtid=i.id)
	    			commentslist.append(comments)
	    		replycommentlist=[]
	    		for i in twt:
	    			reply=Replycomment.objects.filter(replyid=i.id)	
	    			replycommentlist.append(reply)
	    		twtlist=zip(twt,commentslist,replycommentlist)
	    		return render(request, 'updateprofile.html', {'form': form,'twtlist':twtlist,'pic':pic,'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount})  
    except:
    	form =ProfileForm(request.POST)
    	if form.is_valid():
            profile = form.save(commit=False)
            profile.user=request.user
            profile.profile_image = form.cleaned_data['profile_image']
            profile.header_image = form.cleaned_data['header_image']
            profile.save()
            commentslist=[]
            for i in twt:
            	comments=comment.objects.filter(twtid=i.id)
            	commentslist.append(comments)
            replycommentlist=[]	
            for i in twt:
            	reply=Replycomment.objects.filter(replyid=i.id)
            	replycommentlist.append(reply)
            	twtlist=zip(twt,commentslist,replycommentlist)    
            return render(request, 'updateprofile.html', {'form': form,'twtlist':twtlist,'pic':pic,'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount})	
    return render(request, 'updateprofile.html', {'form': form,'pic':pic,'twt1':twt,'followers':followers,'following':following,'twtcount':tweetscount})

def replycomments(request, pk):
		post = get_object_or_404(comment, pk=pk)
		pic=Profile.objects.filter(user=request.user)
		comments=Replycomment.objects.filter(replyid=post.pk)
		twt=comment.objects.filter(user=post.pk)
		return render(request, 'replycomment.html', {'post': twt,'pic':pic,'comment':comments})		

def replysavecomment(request,pk):
	tweets = get_object_or_404(comment, pk=pk)
	if request.method == "POST":
			form=replycommentForm(request.POST,request.FILES)
			if form.is_valid():
					tweet = form.save(commit=False)
					tweet.replyid=get_object_or_404(comment, pk=pk)
					tweet.user=request.user
					tweet.image = form.cleaned_data['image']
					tweet.save()
					return redirect('home')

def comments(request, pk):
		post = get_object_or_404(Tweets, pk=pk)
		pic=Profile.objects.filter(user=request.user)
		comments=comment.objects.filter(twtid=post.pk)
		twt=Tweets.objects.filter(user=post.pk)
		return render(request, 'comments.html', {'post': twt,'pic':pic,'comment':comments})

def savecomment(request,pk):
	tweets = get_object_or_404(Tweets, pk=pk)
	if request.method == "POST":
			form=commentForm(request.POST,request.FILES)
			if form.is_valid():
					tweet = form.save(commit=False)
					tweet.user=request.user
					tweet.twtid=get_object_or_404(Tweets, pk=pk)
					tweet.image = form.cleaned_data['image']
					tweet.save()
					return redirect('home')

def following_page(request,pk):
	user = get_object_or_404(User, pk=pk)
	following_list = Follow.objects.filter(followers=user)
	piclist=[]
	for i in following_list:
		pic=Profile.objects.filter(user=i.following)
		piclist.append(pic)
	mylist=zip(following_list,piclist)
	return render(request,'following_page.html', {'mylist':mylist})

def followers_page(request,pk):
	user = get_object_or_404(User, pk=pk)
	followers_list = Follow.objects.filter(following=user)
	piclist=[]
	for i in followers_list:
		pic=Profile.objects.filter(user=i.followers)
		piclist.append(pic)
	mylist=zip(followers_list,piclist)
	return render(request,'followers_page.html', {'mylist':mylist})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search = request.GET['search']
        po1= User.objects.filter(username__icontains=search)
        piclist=[]
        for i in po1:
        	pic=Profile.objects.filter(user=i.id)
        	piclist.append(pic)
        searchlist=zip(po1,piclist)
        return render(request,'search.html',{'searchlist':searchlist}) 
    else:
        return HttpResponse('Please submit a search term.')

def autocomplete(request):
    if request.is_ajax():
        queryset = User.objects.filter(username__icontains=request.GET.get('search', None)) 
        list = []        

        for i in queryset:
            list.append(i.username)
        data = {
            'list': list,
        }
        return JsonResponse(data)

def about(request):
	return render(request,'about.html', {})
