from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from taggit.models import Tag
from django.views.generic import DetailView, ListView
from .forms import  *
from . import forms
from .forms import CreateArticle, CommentForm


from .models import Article
from django.contrib.auth.decorators import login_required







class TagMixin(object):
    def get_context_data(self,**kwargs):
        context = super(TagMixin,self).get_context_data(**kwargs)
        context['tags']= Tag.objects.all()
        return context

class ArticleIndex(TagMixin,ListView):
    template_name = 'articles/article_list.html'
    model = Article
    paginate_by = '1000'
    queryset = Article.objects.all()
    context_object_name = 'articles'

    ordering = ['-date']




def article_list(request):
    articles = Article.objects.all().order_by('-date');
    query = request.GET.get("q")
    if query:
        articles = articles.filter(title__icontains=query)
    return render(request, 'articles/article_list.html', { 'articles': articles })


def article_detail(request, slug):  # return HttpResponse(slug)
    post = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(post=post).order_by('.date')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            text = request.POST.get('text')
            comment = Comment.objects.create(post=post, author=request.user.username, text=text)
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()
        context={
            'article': post,
            'comments': comments,
            'comment_form': comment_form,
        }

        return  render(request, 'articles/article_detail.html', context)




class TagIndexView(TagMixin,ListView):
    template_name = 'articles/article_list.html'
    model = Article
    paginate_by = '10'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(tags__slug=self.kwargs.get('slug'))


def article_edit(request,id):
    post= get_object_or_404(Article,id=id)
    if post.author !=request.user:
        raise Http404()
    if request.method=="POST":
        form = ArticleEditForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else:
        form = ArticleEditForm(instance=post)
        context={
            'form':form,
            'post':post,
        }
        return  render(request,'articles/article_edit.html',context)

def article_delete(request, id):
    post = get_object_or_404(Article, id=id)
    if post.author != request.user:
        raise Http404()
    post.delete()
    return redirect('/')


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
