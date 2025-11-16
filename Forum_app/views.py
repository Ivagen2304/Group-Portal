from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category, Topic, Message


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categoryes'
    template_name = 'Forum_app/categorylist.html'


class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'Forum_app/topiclist.html'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Topic.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        return context


class MessageListView(ListView):
    model = Message
    context_object_name = 'messages'
    template_name = 'Forum_app/messagelist.html'

    def get_queryset(self):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        return Message.objects.filter(topic=topic)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, pk=self.kwargs['pk'])
        return context
