from Post.views import *
from Post.models import Post

from django.urls import resolve
from django.test import TestCase



class PostURLTest(TestCase):
    def setUp(self):
        Post.objects.create(title="test_title_1", body="test_body_1", status="published")
        self.post = Post.objects.get(title = "test_title_1")

    def test_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_url_resolves_to_list_view(self):
        found = resolve('/post_list')
        self.assertEqual(found.func, post_list)

    def test_url_resolves_to_detail_view(self):
        found = resolve(self.post.get_absolute_url())
        self.assertEqual(found.func, post_detail)
    
    def test_url_resolves_to_about_me(self):
        found = resolve('/about_me')
        self.assertEqual(found.func, about_me)

    
