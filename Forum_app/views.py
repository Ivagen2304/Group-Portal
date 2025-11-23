from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Forum_app/category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Forum_app/category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'Forum_app/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'Forum_app/category_detail.html'
    context_object_name = 'category'



class TopicCreateView(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'Forum_app/topic_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('topic_list', kwargs={'pk': self.object.category.pk})


class TopicUpdateView(UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = 'Forum_app/topic_form.html'

    def get_success_url(self):
        return reverse_lazy('topic_list', kwargs={'pk': self.object.category.pk})


class TopicDeleteView(DeleteView):
    model = Topic
    template_name = 'Forum_app/topic_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('topic_list', kwargs={'pk': self.object.category.pk})


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'Forum_app/topic_detail.html'
    context_object_name = 'topic'



class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'Forum_app/message_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        return {'topic': topic}

    def get_success_url(self):
        return reverse_lazy('message_list', kwargs={'pk': self.object.topic.pk})


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'Forum_app/message_form.html'

    def get_success_url(self):
        return reverse_lazy('message_list', kwargs={'pk': self.object.topic.pk})


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'Forum_app/message_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('message_list', kwargs={'pk': self.object.topic.pk})


class MessageDetailView(DetailView):
    model = Message
    template_name = 'Forum_app/message_detail.html'
    context_object_name = 'message'
