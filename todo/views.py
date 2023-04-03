from django.shortcuts import render

from todo.models import Tag, Task


def index(request):
    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_tags": num_tags,
    }
    return render(request, "todo/index.html", context=context)


