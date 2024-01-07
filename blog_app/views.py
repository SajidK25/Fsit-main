from django.shortcuts import render
from .models import Blog
from django.shortcuts import render, get_object_or_404
# Create your views here.

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_app/blogs.html', {'blogs': blogs})

def blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_app/single-blog.html', {'blog': blog})