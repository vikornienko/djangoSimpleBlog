from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import Post

class PostTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="admin")
        Post.objects.bulk_create([
            Post(title='Title One', slug='title-one', author=User.objects.get(id=1), body="Post awesome text",
                 created_at=timezone.now(), updated_at=timezone.now(), status=Post.status),
            Post(title='Title Two', slug='title-two', author=User.objects.get(id=1), body="Post with Title Two awesome text",
                 created_at=timezone.now(), updated_at=timezone.now(), status=Post.status),
            Post(title='Title Three', slug='title-three', author=User.objects.get(id=1), body="Post with Title Two awesome text",
                 created_at=timezone.now(), updated_at=timezone.now(), status=Post.status),
        ])

    def test_posts_title(self):
        post_one_title = Post.objects.get(id=1)
        post_two_title = Post.objects.get(id=2)
        post_three_title = Post.objects.get(id=3)
        self.assertEquals(post_one_title.title, "Title One")
        self.assertEquals(post_two_title.title, "Title Two")
        self.assertEquals(post_three_title.title, "Title Three")

    def test_post_author(self):
        post_one_author = Post.objects.get(id=1)
        post_two_author = Post.objects.get(id=2)
        post_three_author = Post.objects.get(id=3)
        self.assertEquals(post_one_author.author.username, "admin")
        self.assertEquals(post_two_author.author.username, "admin")
        self.assertEquals(post_three_author.author.username, "admin")


