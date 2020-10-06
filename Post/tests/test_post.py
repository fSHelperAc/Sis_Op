from Post.models import Post

from django.test import TestCase

class PostModelTest(TestCase):
    def test_post_creation(self):
        Post.objects.create(title="test_title_1", body="test_body_1")
        Post(title="test title", body="test body").save()

        posts = Post.objects.all()

        self.assertEqual(posts.count(), 2)

        post = Post.objects.get(title="test title")
        self.assertTrue(post)

        self.assertEqual(post.title,"test title")
        self.assertEqual(post.body,"test body")
        self.assertEqual(post.status, "draft")

    def test_post_update(self):
        Post.objects.create(title="test_title_1", body="test_body_1")
        post = Post.objects.get(title="test_title_1")
        post.body = "test_update"
        post.save()

        post = Post.objects.get(title="test_title_1")
        self.assertEqual(post.body, "test_update")

    def test_post_tag_creation(self):
        Post.objects.create(title="test_title_2", body="test_body_2")
        post = Post.objects.get(title="test_title_2")
        post.tags.add('test_tag')
        self.assertEqual(post.tags.count(),1)

