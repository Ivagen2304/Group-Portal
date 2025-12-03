from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Topic, Post
from .forms import TopicForm, PostForm
from django.contrib.auth.decorators import login_required


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'Forum_app/category_list.html', {'categories': categories})


def topic_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = category.topics.all().order_by('-created_at')
    return render(request, 'Forum_app/topic_list.html', {'category': category, 'topics': topics})


def post_list(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = topic.posts.all().order_by('created_at')
    topic.views += 1
    topic.save()
    return render(request, 'Forum_app/post_list.html', {'topic': topic, 'posts': posts})


@login_required
def create_topic(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        topic_form = TopicForm(request.POST)
        post_form = PostForm(request.POST)
        if topic_form.is_valid() and post_form.is_valid():
            topic = topic_form.save(commit=False)
            topic.category = category
            topic.author = request.user
            topic.save()
            post = post_form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            return redirect('Forum_app:post_list', topic_id=topic.id)
    else:
        topic_form = TopicForm()
        post_form = PostForm()
    return render(request, 'Forum_app/create_topic.html', {'category': category, 'topic_form': topic_form, 'post_form': post_form})


@login_required
def create_post(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            return redirect('Forum_app:post_list', topic_id=topic.id)
    else:
        form = PostForm()
    return render(request, 'Forum_app/create_post.html', {'topic': topic, 'form': form})
