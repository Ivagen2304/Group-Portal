from django.urls import path
from . import views
app_name = 'moderation'
urlpatterns = [
    path('create/', views.create_poll, name='create_poll'),
    path('polls/', views.poll_list, name='poll_list'),
    path('notifications/', views.notifications, name='notifications'),
    path('notification_detail/<int:pk>/', views.notification_detail, name='notification_detail'),
    path('poll/<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
]
