from django.shortcuts import render
from django.views import generic

from todo.models import Tag, Task
from todo.forms import TagForm, TaskForm


def index(request):
    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_tags": num_tags,
    }
    return render(request, "todo/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    form_class = TagForm


class TaskListView(generic.ListView):
    model = Task
    form_class = TaskForm
