from django.shortcuts import render
from .models import Blog
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def blogs(request):
    blog_list = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 5)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'blog_app/blogs.html', {'blogs': blogs})

def blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_app/single-blog.html', {'blog': blog})