from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'detail_blog':detail_blog})
