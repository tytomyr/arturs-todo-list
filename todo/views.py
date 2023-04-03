from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Tag, Task
from todo.forms import TagForm, TaskForm


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TaskListView(generic.ListView):
    model = Task
    form_class = TaskForm
    template_name = "todo/index.html"
