from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def index(request):
    blogs = BlogPost.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


def blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog.html', context)


@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if blog.owner != request.user:
        owner = False
    else:
        owner = True

    if request.method != 'POST':
        form = BlogPostForm(instance=blog)
    else:
        form = BlogPostForm(instance=blog, data=request.POST)
        form.save()
        return redirect('blogs:blog', blog.id)

    context = {'form': form, 'blog': blog, 'owner': owner}
    return render(request, 'blogs/edit_blog.html', context)


def my_blogs(request):
    blogs = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/my_blogs.html', context)
