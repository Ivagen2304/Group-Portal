from django.contrib import admin
from .models import Category, Topic, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'views')
    list_filter = ('category', 'author')
    search_fields = ('title', 'author__username')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'author', 'created_at')
    list_filter = ('topic', 'author')
    search_fields = ('content', 'author__username')
