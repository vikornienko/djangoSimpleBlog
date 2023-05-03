from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique_for_date='publish_at')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        # Define the order: the most recent posts are shown first.
        ordering = ['-publish_at']
        # Indexing the database by field publish_at.
        # https://docs.djangoproject.com/en/4.1/ref/models/indexes/
        indexes = [
            models.Index(fields=['-publish_at'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish_at.year,
                             self.publish_at.month,
                             self.publish_at.day,
                             self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='coments')
    name = models.CharField(max_length=64)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']
        indexes = [models.Index(fields=['created_at']),]

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
