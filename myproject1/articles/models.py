from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None)

    tags = TaggableManager()


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #approved_comment = models.BooleanField(default=False)

    #def approve(self):
         #self.approved_comment = True
          #self.save()

    def __str__(self):
        return '{}.{}'.format(self.post.title, str(self.author))

