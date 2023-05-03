from django.contrib import admin

from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish_at', 'status']
    list_filter = ['status', 'created_at', 'publish_at', 'author']
    search_fields = ['title', 'body', 'author']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish_at'
    ordering = ['status', 'publish_at']
    list_editable = ['status']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created_at', 'active']
    list_filter = ['active', 'created_at', 'updated_at']
    search_fields = ['name', 'email', 'body']

