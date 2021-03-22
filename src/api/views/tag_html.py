from django.shortcuts import render
from api.models import Tag, Post
from api.serializers import PostListSerializers
from rest_framework.response import Response
from api.forms import TagForm

def tag_detail_list(request, tag_id):
    posts = Post.objects.filter(tags__id = tag_id)
    print(posts)
    if posts:
        ser = PostListSerializers(posts, many = True)
        return render(request, 'post_list.html', {'posts': posts})
    return render(request,'post_list.html', {'data': 'error'})

def tag_create(request):
    form = TagForm()
    if request.method == 'POST':
        print(request.POST)
        save_form = TagForm(request.POST)
        save_form = save_form.save()
        # Post.objects.create(title = request.POST['title'], body = request.POST['body'], tags = *request.POST['tags'])
        print(Tag.objects.last())
    return render(request, 'tag_create.html', {'form': form})

def tag_delete(request, tag_id):
    print(tag_id)
    Tag.objects.get(id = tag_id).delete()
    return render(request, 'tag_list.html', {'tags': Tag.objects.all()})