from django.test  import SimpleTestCase

from django.urls import reverse, resolve

from articles import admin
from articles.views import article_create
from myproject.views import about
from contact.views import contact
from  articles.views import *
from accounts.views import *
class TestUrls(SimpleTestCase):

     def test_about(self):
         url=reverse("about")
         self.assertEquals(resolve(url).func, about)

     def test_create(self):
         url = reverse("articles:create")
         self.assertEquals(resolve(url).func, article_create)

     def test_contact(self):
        url = reverse("contact")
        self.assertEquals(resolve(url).func, contact)

     def test_articles(self):
        url = reverse("articles:list")
        self.assertEquals(resolve(url).func.view_class, ArticleIndex)

     def test_home(self):
         url = reverse("home")
         self.assertEquals(resolve(url).func,article_list)

     def test_signup(self):
         url = reverse("accounts:signup")
         self.assertEquals(resolve(url).func, signup_view)

     def test_login(self):
         url = reverse("accounts:login")
         self.assertEquals(resolve(url).func, login_view)

     def test_logout(self):
         url = reverse("accounts:logout")
         self.assertEquals(resolve(url).func, logout_view)

     def article_Edit(self):
         url = reverse("articles:article_edit")
         self.assertEquals(resolve(url).func, article_edit)









