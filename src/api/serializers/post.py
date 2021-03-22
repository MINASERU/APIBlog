from rest_framework import serializers
from api.models import Post, Tag
from .tag import TagPostSerializer

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id', )

class PostListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('tags', 'body',)

class Post_detailListSerializers(serializers.ModelSerializer):
    def update(self, instance, data):
        tags = data.pop('tags', [])
        instance = super(Post_detailListSerializers, self).update(instance, data)
        if tags:
            post_tags = instance.tags.all().values_list('id', flat = True)
            for tag in tags:
                if tag not in post_tags:
                    instance.tags.add(tag)
                    instance.save()
        return instance
        
    class Meta:
        model = Post
        exclude = ('id', )
    
    

        


