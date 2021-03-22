from django.shortcuts import render
from api.models import Post
from api.serializers import PostListSerializers, Post_detailListSerializers, PostCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = Post_detailListSerializers
    queryset = Post.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'

class PostListView(ListAPIView):
    serializer_class = PostListSerializers
    queryset = Post.objects.all()

# @api_view(['GET'])
# def posts(request):
#     posts = Post.objects.all()
#     ser = PostListSerializers(posts, many = True)
#     return Response({'data': ser.data})

@api_view(['GET'])
def post_details(request, post_id):
    post = Post.objects.get(id = post_id)
    ser = Post_detailListSerializers(post)
    return Response({'data': ser.data})