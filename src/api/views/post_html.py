from django.shortcuts import render, redirect
from api.forms import PostForm
from api.models import Post, Tag

def posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author_id=request.user)
    else:
        posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post_details(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    error = ''
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                note = form.save(commit = False)
                note.author = request.user
                note.save()
                return redirect('api:home')
            else:
                error = 'Форма была неверной'

        form = PostForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'post_create.html', context)
    return redirect( 'authe:login')