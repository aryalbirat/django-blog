from rest_framework import serializers
from .models import Post


class PostSerialisers(serializers.Serializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content"]
        
