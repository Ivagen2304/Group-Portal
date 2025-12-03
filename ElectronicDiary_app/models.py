from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Учень'),
        ('teacher', 'Вчитель'),
        ('parent', 'Батько/мати'),
        ('admin', 'Адміністратор'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"



class Class(models.Model):
    name = models.CharField(max_length=20)  
    year = models.PositiveIntegerField()
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='class_teacher')

    def __str__(self):
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} — {self.subject.name if self.subject else 'Без предмету'}"



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    parent_contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.get_full_name()



class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    topic = models.CharField(max_length=255)
    homework = models.TextField(blank=True)

    def __str__(self):
        return f"{self.subject.name} — {self.date}"



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField()
    comment = models.CharField(max_length=255, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.last_name}: {self.grade}"



class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Присутній'),
        ('absent', 'Відсутній'),
        ('late', 'Запізнився'),
    ]
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='present')
    comment = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.student.user.last_name} — {self.get_status_display()}"


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    child = models.ForeignKey(Student, on_delete=models.CASCADE)
    relation = models.CharField(max_length=20, default='parent')

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.relation})"



class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    school_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
