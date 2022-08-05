from django import forms
from . import models
from .models import Article, Comment
from django.contrib.auth.models import User

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb','tags']


class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb','tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)