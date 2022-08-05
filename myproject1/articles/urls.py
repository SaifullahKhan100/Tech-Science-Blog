from django.conf.urls import url
from . import views
from .views import TagIndexView,ArticleIndex

app_name = 'articles'

urlpatterns = [
    url(r'(?P<id>\d+)/article_edit/$', views.article_edit, name="article_edit"),
    url(r'(?P<id>\d+)/article_delete/$', views.article_delete, name="article_delete"),
    url(r'^$', ArticleIndex.as_view(), name="list"),
    url(r'^$', views.article_list, name="List"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagIndexView.as_view(), name='tagged'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]