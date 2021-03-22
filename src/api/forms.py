from .models import Post, Tag
from django.forms import ModelForm, TextInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введите название'
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            })
        }
        exclude = ('id', 'author')

class TagForm(ModelForm):
    class Meta:
        model = Tag
        widgets = {
            'name': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите название'
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            })
        }
        exclude = ('id', )