from django.shortcuts import render
from blog.models import Blog

def home(request):
    latest_posts = Blog.objects.filter(status='published').order_by('-created_at')[:3]
    return render(request,'home.html',{'latest_posts': latest_posts})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def resume(request):
    return render(request, 'resume/resume.html')

