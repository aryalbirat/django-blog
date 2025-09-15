# from django.shortcuts import render
from rest_framework.response import Response
from .models import Post
from django.http import HttpResponse
from .serializers import PostSerialisers


# @api_view(["GET"])
def post_list(request):
    print("This is the request:", request)
    posts = Post.objects.all().order_by("-created_at")  # descending order
    serialiser = PostSerialisers(posts, many=True)
    print("This is the posts:", serialiser, " And the data is: ", serialiser.data)
    # return render(request, "blog/post_list.html", {"posts": posts})
    return Response(serialiser.data)


def post_detail(request, id):
    posts = Post.objects.get(id=id)
    serialiser = PostSerialisers(posts)
    return Response(serialiser.data)


def default_route(request):
    return HttpResponse("Hello, this is the home screen")
