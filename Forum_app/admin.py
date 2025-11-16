from django.contrib import admin
from .models import Category, Topic, Message

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_at', 'views', 'is_closed']
    list_filter = ['category', 'is_closed', 'created_at']
    search_fields = ['title']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['topic', 'author', 'created_at', 'is_edited']
    list_filter = ['created_at', 'is_edited']
    search_fields = ['text']