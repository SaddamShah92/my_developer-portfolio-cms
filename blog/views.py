from django.shortcuts import render

def blog(request):
    return render(request, 'blog/blog.html')

def blog_detail(request, pk):
    return render(request, 'blog/blog_detail')
