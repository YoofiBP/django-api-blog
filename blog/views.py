from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly

# Create your views here.


class PostIndex(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostShow(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
