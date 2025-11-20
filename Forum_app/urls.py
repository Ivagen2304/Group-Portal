from django.urls import path
from .views import *

urlpatterns = [
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

    path('topic/create/', TopicCreateView.as_view(), name='topic_create'),
    path('topic/<int:pk>/edit/', TopicUpdateView.as_view(), name='topic_edit'),
    path('topic/<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),

    path('topic/<int:pk>/message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_edit'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
]