from django.shortcuts import render, get_object_or_404, redirect

from .models import (
    Student, Teacher, Class, Subject,
    Lesson, Grade, Attendance, Parent, Announcement
)

from .forms import (
    StudentForm, TeacherForm, ClassForm, SubjectForm,
    LessonForm, GradeForm, AttendanceForm, ParentForm,
    AnnouncementForm
)

# =========================================================
# Универсальные функции
# =========================================================

def universal_list(request, model, template, context_name="items"):
    items = model.objects.all()
    return render(request, template, {context_name: items})


def universal_detail(request, model, pk, template, context_name="item"):
    item = get_object_or_404(model, pk=pk)
    return render(request, template, {context_name: item})


def universal_create(request, form_class, redirect_url, template):
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class()

    return render(request, template, {"form": form})


def universal_update(request, model, form_class, pk, redirect_url, template):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = form_class(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=item)

    return render(request, template, {"form": form})


def universal_delete(request, model, pk, redirect_url, template):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        item.delete()
        return redirect(redirect_url)

    return render(request, template, {"item": item})


# =========================================================
# STUDENTS
# =========================================================

def student_list(request):
    return universal_list(
        request,
        Student,
        "ElectronicDiary_app/student_list.html",
        "students"
    )


def student_detail(request, pk):
    return universal_detail(
        request,
        Student,
        pk,
        "ElectronicDiary_app/student_detail.html",
        "student"
    )


def student_create(request):
    return universal_create(
        request,
        StudentForm,
        "student_list",
        "ElectronicDiary_app/student_form.html"
    )


def student_update(request, pk):
    return universal_update(
        request,
        Student,
        StudentForm,
        pk,
        "student_list",
        "ElectronicDiary_app/student_form.html"
    )


def student_delete(request, pk):
    return universal_delete(
        request,
        Student,
        pk,
        "student_list",
        "ElectronicDiary_app/student_confirm_delete.html"
    )


# =========================================================
# TEACHERS
# =========================================================
# ❗ Ты должен создать папку:
# ElectronicDiary_app/templates/teachers/
# и 4 файла: list.html, detail.html, form.html, delete.html

def teacher_list(request):
    return universal_list(request, Teacher, "teachers/list.html", "teachers")

def teacher_detail(request, pk):
    return universal_detail(request, Teacher, pk, "teachers/detail.html", "teacher")

def teacher_create(request):
    return universal_create(request, TeacherForm, "teacher_list", "teachers/form.html")

def teacher_update(request, pk):
    return universal_update(request, Teacher, TeacherForm, pk, "teacher_list", "teachers/form.html")

def teacher_delete(request, pk):
    return universal_delete(request, Teacher, pk, "teacher_list", "teachers/delete.html")


# =========================================================
# CLASSES
# =========================================================

def class_list(request):
    return universal_list(request, Class, "classes/list.html", "classes")

def class_detail(request, pk):
    return universal_detail(request, Class, pk, "classes/detail.html", "class")

def class_create(request):
    return universal_create(request, ClassForm, "class_list", "classes/form.html")

def class_update(request, pk):
    return universal_update(request, Class, ClassForm, pk, "class_list", "classes/form.html")

def class_delete(request, pk):
    return universal_delete(request, Class, pk, "class_list", "classes/delete.html")


# =========================================================
# SUBJECTS
# =========================================================

def subject_list(request):
    return universal_list(request, Subject, "subjects/list.html", "subjects")

def subject_detail(request, pk):
    return universal_detail(request, Subject, pk, "subjects/detail.html", "subject")

def subject_create(request):
    return universal_create(request, SubjectForm, "subject_list", "subjects/form.html")

def subject_update(request, pk):
    return universal_update(request, Subject, SubjectForm, pk, "subject_list", "subjects/form.html")

def subject_delete(request, pk):
    return universal_delete(request, Subject, pk, "subject_list", "subjects/delete.html")


# =========================================================
# LESSONS
# =========================================================

def lesson_list(request):
    return universal_list(request, Lesson, "lessons/list.html", "lessons")

def lesson_detail(request, pk):
    return universal_detail(request, Lesson, pk, "lessons/detail.html", "lesson")

def lesson_create(request):
    return universal_create(request, LessonForm, "lesson_list", "lessons/form.html")

def lesson_update(request, pk):
    return universal_update(request, Lesson, LessonForm, pk, "lesson_list", "lessons/form.html")

def lesson_delete(request, pk):
    return universal_delete(request, Lesson, pk, "lesson_list", "lessons/delete.html")


# =========================================================
# GRADES
# =========================================================

def grade_list(request):
    return universal_list(request, Grade, "grades/list.html", "grades")

def grade_detail(request, pk):
    return universal_detail(request, Grade, pk, "grades/detail.html", "grade")

def grade_create(request):
    return universal_create(request, GradeForm, "grade_list", "grades/form.html")

def grade_update(request, pk):
    return universal_update(request, Grade, GradeForm, pk, "grade_list", "grades/form.html")

def grade_delete(request, pk):
    return universal_delete(request, Grade, pk, "grade_list", "grades/delete.html")


# =========================================================
# ATTENDANCE
# =========================================================

def attendance_list(request):
    return universal_list(request, Attendance, "attendance/list.html", "attendance_list")

def attendance_detail(request, pk):
    return universal_detail(request, Attendance, pk, "attendance/detail.html", "attendance")

def attendance_create(request):
    return universal_create(request, AttendanceForm, "attendance_list", "attendance/form.html")

def attendance_update(request, pk):
    return universal_update(request, Attendance, AttendanceForm, pk, "attendance_list", "attendance/form.html")

def attendance_delete(request, pk):
    return universal_delete(request, Attendance, pk, "attendance_list", "attendance/delete.html")


# =========================================================
# PARENTS
# =========================================================

def parent_list(request):
    return universal_list(request, Parent, "parents/list.html", "parents")

def parent_detail(request, pk):
    return universal_detail(request, Parent, pk, "parents/detail.html", "parent")

def parent_create(request):
    return universal_create(request, ParentForm, "parent_list", "parents/form.html")

def parent_update(request, pk):
    return universal_update(request, Parent, ParentForm, pk, "parent_list", "parents/form.html")

def parent_delete(request, pk):
    return universal_delete(request, Parent, pk, "parent_list", "parents/delete.html")


# =========================================================
# ANNOUNCEMENTS
# =========================================================

def announcement_list(request):
    return universal_list(request, Announcement, "announcements/list.html", "announcements")

def announcement_detail(request, pk):
    return universal_detail(request, Announcement, pk, "announcements/detail.html", "announcement")

def announcement_create(request):
    return universal_create(request, AnnouncementForm, "announcement_list", "announcements/form.html")

def announcement_update(request, pk):
    return universal_update(request, Announcement, AnnouncementForm, pk, "announcement_list", "announcements/form.html")

def announcement_delete(request, pk):
    return universal_delete(request, Announcement, pk, "announcement_list", "announcements/delete.html")
