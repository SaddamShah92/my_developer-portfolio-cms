from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog(request):
    posts = Blog.objects.filter(status = 'published')
    featured_post = Blog.objects.filter(is_featured = True, status = 'published').first()

    context = {
        'posts': posts,
        'featured_post' : featured_post,
    }

    return render(request, 'blog/blog.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug = slug, status = 'published')

    context = {
        'post' : post,
    }
    return render(request, 'blog/blog_detail.html', context)
