from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'classes', views.ClassViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'grades', views.GradeViewSet)
router.register(r'attendance', views.AttendanceViewSet)
router.register(r'parents', views.ParentViewSet)
router.register(r'announcements', views.AnnouncementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
