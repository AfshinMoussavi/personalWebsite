from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from website.models import Contace
def blog_view(request, cat_name = None, author_username = None):
    posts = Post.objects.filter(status = 1)
    if cat_name:
        posts = posts.filter(category__name = cat_name)
    
    if author_username:
        posts = posts.filter(author__username=author_username)
    
    posts = Paginator(posts, 1)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
         posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {
        'posts':posts
    }
    return render(request, 'blog/blog-home.html', context)
    

def blog_single_view(request, pid):
    post = get_object_or_404(Post, id=pid, status=1)
    context = {
        'post':post 
    }
    return render(request, 'blog/blog-single.html', context)

def blog_category_view(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name = cat_name)
    context = {
        'posts':posts
    }
    return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
        if request.GET.get('s'):
            posts = posts.filter(content__contains=request.GET.get('s'))
    print(f'the request is => {request}')
    context = {
        'posts':posts
    }
    return render(request, 'blog/blog-home.html', context)
