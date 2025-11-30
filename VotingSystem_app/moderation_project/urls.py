from django.contrib import admin
from django.urls import path, include
from moderation import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('moderation/', include('moderation.urls')),
    path('poll/<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
    path('notification_detail/<int:pk>/', views.notification_detail, name='notification_detail'),
]
