from Post.views import *
from Post.models import Post, Comment

from django.urls import resolve
from django.test import TestCase



class PostViewTest(TestCase):

    def setUp(self):
        for i in range(0,10):
            Post.objects.create(title="test_title_"+str(i), body="test_body_"+str(i), status="published")
       
        Post.objects.create(title="test_draft_title_1", body="test_draft_body_1")
        self.post = Post.objects.get(title = "test_title_1")
        Comment.objects.create(author="person_test_1", body="test_comment_body_1", post=self.post)
        self.post_draft = Post.objects.get(title = "test_draft_title_1")

    # Check for correct html

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_detail_post_returns_correct_html(self):
        response = self.client.get(self.post.get_absolute_url())
        
        self.assertTemplateUsed(response, 'post/detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_post_returns_correct_html(self):
        response = self.client.get('/post_list')
        self.assertTemplateUsed(response, 'post/list.html')
        self.assertTemplateUsed(response, 'post/post_list.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_about_me_returns_correct_html(self):
        response = self.client.get('/about_me')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'about_me.html')

    ## Check Post in Pages

    # TODO Cambiar este test teniendo en cuenta el paginator
    """def test_posts_in_homepage(self):
        response = self.client.get('/')
        self.assertIn('test_title_', response.content.decode())
        self.assertNotIn('test_draft_title_1', response.content.decode())
    """

    def test_post_in_post_detail(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertIn('test_title_1', response.content.decode())
        self.assertIn('test_body_1', response.content.decode())

    ##Check for pagintor in Pages

    def test_paginator_in_post_list(self):
        response = self.client.get('/post_list')
        self.assertEquals(len(response.context['posts']), 5)
    ## Check Draft Post not in Pages

    def test_draft_post_not_post_detail(self):
        response = self.client.get(self.post_draft.get_absolute_url())
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_post_list(self):
        response = self.client.get('post_list')
        self.assertNotIn("test_draft_title_1", response.content.decode()) 

    def test_draft_post_not_homepage(self):
        response = self.client.get('/')
        self.assertNotIn("test_draft_title_1", response.content.decode()) 

    def test_comment_in_post_detail(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertIn('test_comment_body_1', response.content.decode())
    
    def test_post_comment(self):
        self.assertEqual(Comment.objects.count(), 1)
        response = self.client.post(self.post.get_absolute_url(),
                    data={'author':'test_comment_post_author',
                        'body':'test_comment_post_body'})
        self.assertEqual(Comment.objects.count(), 2)
        response = self.client.get(self.post.get_absolute_url())
        self.assertIn('test_comment_post_author', response.content.decode())
    
    
    