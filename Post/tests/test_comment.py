from Post.models import Post, Comment

from django.test import TestCase

class CommentModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title="test_title_1", body="test_body_1")
        self.post = Post.objects.first()

    def test_create_comment(self):
        Comment.objects.create(author="person_test_1", body="test_comment_body_1", post=self.post)
        self.assertEqual(Comment.objects.count(), 1)
        com = Comment.objects.first()
        self.assertEqual(com.author, "person_test_1")
        self.assertEqual(com.body, "test_comment_body_1")
        self.assertEqual(self.post, com.post)

    def test_create_multiple_comments(self):
        Comment.objects.create(author="person_test_1", body="test_comment_body_1", post=self.post)
        Comment.objects.create(author="person_test_2", body="test_comment_body_2", post=self.post)
        Comment.objects.create(author="person_test_3", body="test_comment_body_3", post=self.post)
        
        self.assertEqual(Comment.objects.filter(post=self.post).count(), 3
            ,"Before comment creation")
        self.assertEqual(Comment.objects.count(), 3)

        Post.objects.create(title="test_title_2", body="test_body_2")
        post_test_1 = Post.objects.first()
        Comment.objects.create(author="person_test_4", body="test_body_4", post=post_test_1)

        self.assertEqual(Comment.objects.filter(post=self.post).count(), 3
            ,"After comment creation")
        self.assertEqual(Comment.objects.filter(post=post_test_1).count(), 1)
        self.assertEqual(Comment.objects.count(), 4)

    def test_comment_linkage(self):
        Comment.objects.create(author="person_test_1", body="test_comment_body_1", post=self.post)
        comment_to_parent = Comment.objects.first()
        Comment.objects.create(author="person_test_2", body="test_comment_body_2",
             post=self.post, comment_parent = comment_to_parent)
        self.assertEqual(Comment.objects.count(), 2)

        self.assertEqual(Comment.objects.filter(comment_parent=comment_to_parent).count(),1)

