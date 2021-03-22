from django.db import models
from authe.models import Author 

# Create your models here.
class Tag(models.Model):
    name = models.TextField(max_length = 500, verbose_name = 'Имя')
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэги'


class Post(models.Model):
    title = models.TextField(max_length = 1000, verbose_name = 'Заголовок')
    body = models.TextField(max_length = 5000, verbose_name = 'Тело')
    tags = models.ManyToManyField(Tag, verbose_name = 'Тэги')
    author = models.ForeignKey(Author, related_name = 'posts', on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'

