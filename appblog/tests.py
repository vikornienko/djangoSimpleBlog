from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory,TestCase
from django.utils import timezone

from .models import Post
from .views import PostListView, post_detail

# Class for app models testing
class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", email="test1@ex.com", password="mega_top_secret")
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

# Class for app views testing
class PostListViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_list_view(self):
        request_list_view = self.factory.get("/appblog/post/list")
        request_list_view.user = AnonymousUser()

        response_list_view = PostListView.as_view()(request_list_view)
        self.assertEquals(response_list_view.status_code, 200)

    def test_post_detail(self):
        request_post_detail = self.factory.get()
