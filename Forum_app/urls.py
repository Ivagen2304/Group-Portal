from django.urls import path
from . import views

app_name = 'Forum_app'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', views.post_list, name='post_list'),
    path('category/<int:category_id>/create_topic/', views.create_topic, name='create_topic'),
    path('topic/<int:topic_id>/create_post/', views.create_post, name='create_post'),
]
