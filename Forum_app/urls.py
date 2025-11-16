from .views import *
from django.urls import path, include


urlpatterns = [
    path('', CategoryListView.as_view(), name='categorylist'),
    path('category/<int:pk>/', TopicListView.as_view(), name='topiclist'),
    path('topic/<int:pk>/', MessageListView.as_view(), name='messagelist')
]