from django.shortcuts import render
from api.models import Tag, Post
from api.serializers import TagListSerializers, PostListSerializers, TagCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

class TagCreateView(CreateAPIView):
    serializer_class = TagCreateSerializer

class TagDetailView(RetrieveAPIView):
    serializer_class = PostListSerializers
    queryset = Post.objects.all()
    lookup_field = 'tags__id'
    lookup_url_kwarg = 'tag_id'

class TagListView(ListAPIView):
    serializer_class = TagListSerializers
    queryset = Tag.objects.all()

@api_view(['GET'])
def tags(request):
    tags = Tag.objects.all()
    ser = TagListSerializers(tags, many = True)
    # for tag in tags:
    #     a.append({'name': tag.name, 'id': tag.id})
    # return Response({'data': ser.data})
    return render(request, 'tag_list.html', {'tags': tags})

@api_view(['GET'])
def tag_details(request, tag_id):
    posts = Post.objects.filter(tags__id = tag_id)
    print(posts)
    if posts:
        ser = PostListSerializers(posts, many = True)
        # for post in posts:
        #     a.append({'title': post.title, 'body': post.body})

        # return render(request, 'index.html', {'data': ser.data})
        return Response({'data': ser.data})
    return Response({'data': 'error'})
