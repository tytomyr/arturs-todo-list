from django.shortcuts import render
from django.views import generic

from todo.models import Tag, Task
from todo.forms import TagForm, TaskForm


class TagListView(generic.ListView):
    model = Tag
    form_class = TagForm


class TaskListView(generic.ListView):
    model = Task
    form_class = TaskForm
    template_name = "todo/index.html"
