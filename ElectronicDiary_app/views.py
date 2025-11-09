from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User, Student, Teacher, Class, Subject, Lesson, Grade, Attendance, Parent, Announcement
from .serializers import (
    UserSerializer, StudentSerializer, TeacherSerializer, ClassSerializer,
    SubjectSerializer, LessonSerializer, GradeSerializer, AttendanceSerializer,
    ParentSerializer, AnnouncementSerializer
)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('user', 'school_class').all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]



class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related('user', 'subject').all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]



class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.select_related('teacher').all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticated]



class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]



class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.select_related('subject', 'teacher', 'school_class').all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]



class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.select_related('student', 'lesson').all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]



class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related('student', 'lesson').all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]



class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.select_related('user', 'child').all()
    serializer_class = ParentSerializer
    permission_classes = [permissions.IsAuthenticated]



class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.select_related('author', 'school_class').all()
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticated]

