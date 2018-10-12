from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
# Create your views here.
def post_list(request):
    total = Post.objects.count()
    totalpages = total/10;
    records_per_page = 2;
    page = request.GET.get('page')

    if page and int(page) > 1:
        #offset = (page - 1) * 10;
        page = int(page)
        limit = int(page) * records_per_page
        offset = limit - records_per_page
    else:
        offset = 0
        limit = 10

    contact_list = Post.objects.all()[offset:limit]
    paginator = Paginator(contact_list, records_per_page) # Show 25 contacts per page
    #import ipdb
    #ipdb.set_trace()
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#for search bar
def search_form(request):
        if 'search' in request.GET and request.GET['search']:
            search = request.GET['search']
            posts =Post.objects.filter(title__startswith = search)
            return render(request, 'blog/post_list.html', {'posts': posts})
        else:
            return HttpResponse('Please submit a search term.')
# for auto text 

def autocomplete(request):
    posts = Post.objects.filter(title__startswith=request.GET['search'])
    results = []
    for i in posts:
        results.append(i.title)
    data = {
       'list': results,
    }
    return JsonResponse(data)

