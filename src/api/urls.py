from django.urls import path
from .views import tags, posts, tag_details,  post_details, PostListView, PostDetailView, TagDetailView, PostCreateView, TagCreateView, post_details, tag_detail_list, post_create, tag_create, tag_delete


app_name = 'api'

urlpatterns = [
    path('tags/', tags, name = 'tag_list'),
    path('posts/',PostListView.as_view()),
    path('tag/<int:tag_id>', TagDetailView.as_view()),
    path('post/<int:post_id>', PostDetailView.as_view()),
    path('home', posts, name = 'home'), 
    path('create/post', PostCreateView.as_view()),
    path('create/tag', TagCreateView.as_view()),
    path('posts/<int:post_id>', post_details, name = 'post_detail'),
    path('taglist/<int:tag_id>', tag_detail_list, name = 'tag_detail'),
    path('post/create', post_create, name = 'post_create'),
    path('tag/create', tag_create, name = 'tag_create'),
    path('tag/delete/<int:tag_id>', tag_delete, name = 'tag_delete'),
    

]