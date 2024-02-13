from django.shortcuts import render
from .models import post
# Create your views here.
def index(request) :
    posts = post.objects.all()
    return render(request, 'index.html', {'posts' : posts})


def post_fun(request, pk) :
    posts = post.objects.get(id=pk)
    return render(request, 'post_fun.html', {'posts' : posts})
