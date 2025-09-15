from django.shortcuts import render
from .models import Post


def post_list(request):
    print("This is the request:", request)
    posts = Post.objects.all().order_by("-created_at")
    print("This is the posts:", posts)
    return render(request, "blog/post_list.html", {"posts": posts})
