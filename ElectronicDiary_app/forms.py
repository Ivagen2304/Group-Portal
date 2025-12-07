from django import forms
from .models import (
    Student, Teacher, Class, Subject,
    Lesson, Grade, Attendance, Parent, Announcement
)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'grade', 'birth_date']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'subject', 'position']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'year', 'teacher']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'school_class', 'teacher', 'date', 'topic', 'homework']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'lesson', 'grade', 'comment']


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['lesson', 'student', 'status', 'comment']


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['user', 'child', 'relation']


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'author', 'school_class']
