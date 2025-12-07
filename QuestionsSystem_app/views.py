from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Category, Answer
from .forms import QuestionForm, CategoryForm, AnswerForm


def category_list(request):
    categories = Category.objects.all()
    return render(request, "QuestionsSystem_app/category_list.html", {
        "categories": categories
    })


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    questions = Question.objects.filter(category=category)
    return render(request, "QuestionsSystem_app/category_detail.html", {
        "category": category,
        "questions": questions
    })


@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()

    return render(request, "QuestionsSystem_app/category_form.html", {
        "form": form
    })


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category.delete()
        return redirect("category_list")

    return render(request, "QuestionsSystem_app/categoty_delete.html", {
        "category": category
    })




def question_list(request):
    categories = Category.objects.all()
    questions = Question.objects.all().order_by("-created_at")

    return render(request, "QuestionsSystem_app/question_list.html", {
        "categories": categories,
        "questions": questions,
    })


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question=question).order_by("-created_at")

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("/auth/login/")

        form = AnswerForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.author = request.user
            ans.question = question
            ans.save()
            return redirect("question_detail", pk=pk)
    else:
        form = AnswerForm()

    return render(request, "QuestionsSystem_app/question_detail.html", {
        "question": question,
        "answers": answers,
        "form": form,
    })


@login_required
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.author = request.user
            q.save()
            return redirect("question_list")
    else:
        form = QuestionForm()

    return render(request, "QuestionsSystem_app/question_form.html", {"form": form})


@login_required
def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.user != question.author:
        return redirect("question_detail", pk=pk)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("question_detail", pk=pk)
    else:
        form = QuestionForm(instance=question)

    return render(request, "QuestionsSystem_app/question_form.html", {"form": form})


@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.user != question.author:
        return redirect("question_detail", pk=pk)

    if request.method == "POST":
        question.delete()
        return redirect("question_list")

    return render(request, "QuestionsSystem_app/question_delete.html", {
        "question": question
    })
