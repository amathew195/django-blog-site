from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
import lorem

# Create your views here.
blogs = {
"blog1": lorem.paragraph(),
"blog2": lorem.paragraph(),
"blog3": lorem.paragraph()
}

def index(request):
    return render(request, 'blog/index.html', {"blogs": blogs})

def posts(request):
    return render(request, 'blog/posts.html', {"blogs": blogs})

def posts_detail(request, slug):
    blog_name = slug
    blog = blogs[slug]
    return render(request, 'blog/post_detail.html', {
        "blog": blog,
        "blog_name": blog_name
        })