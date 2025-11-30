from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView,
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView,

    TopicListView, TopicDetailView,
    TopicCreateView, TopicUpdateView, TopicDeleteView,

    MessageListView, MessageDetailView,
    MessageCreateView, MessageUpdateView, MessageDeleteView,
)

urlpatterns = [
    # CATEGORY
    path("", CategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    path("category/<int:pk>/update/", CategoryUpdateView.as_view(), name="category_update"),
    path("category/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),

    # TOPIC LIST (главная часть форума)
    path("category/<int:pk>/topics/", TopicListView.as_view(), name="topic_list"),

    # TOPIC CRUD
    path("category/<int:pk>/topics/create/", TopicCreateView.as_view(), name="topic_create"),
    path("topic/<int:pk>/", TopicDetailView.as_view(), name="topic_detail"),
    path("topic/<int:pk>/update/", TopicUpdateView.as_view(), name="topic_update"),
    path("topic/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic_delete"),

    # MESSAGE LIST
    path("topic/<int:pk>/messages/", MessageListView.as_view(), name="message_list"),

    # MESSAGE CRUD
    path("topic/<int:pk>/messages/create/", MessageCreateView.as_view(), name="message_create"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("message/<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),
]
