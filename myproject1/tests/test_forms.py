from django.test import SimpleTestCase
from articles.forms import CommentForm, CreateArticle, ArticleEditForm


class Comment_test_forms(SimpleTestCase):

    def test_comment_form_valid_data(self):
        form = CommentForm(data=
                           {
                               'content': 'Yo wassup'
                           }



                           )
        self.assertTrue(form.is_valid())


    def test_comment_form_no_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)








class Create_forms(SimpleTestCase):

    def test_create_form_valid_data(self):
        form = CreateArticle(data=
                           {
                               'title': 'Ashiq',
                               'body':'cool dude',
                               'slug':'asdasf'
                           }



                           )
        self.assertTrue(form.is_valid())


    def test_create_form_no_data(self):
        form = CreateArticle(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)







