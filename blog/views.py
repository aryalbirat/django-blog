from django.shortcuts import render

from .models import Post
from django.http import HttpResponse


def post_list(request):
    print("This is the request:", request)
    posts = Post.objects.all().order_by("-created_at")
    print("This is the posts:", posts)
    return render(request, "blog/post_list.html", {"posts": posts})


def default_route(request):
    return HttpResponse("Hello, this is the home screen")
