from django.urls import path
from .views import (TagListView,
                    TaskListView,
                    TagCreateView,
                    TagDeleteView,
                    TaskCreateView,
                    TaskDeleteView,
                    complete_task,
                    TaskUpdateView,
                    TagUpdateView,)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("admin/", TaskListView.as_view(), name="admin"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("<int:pk>/status/", complete_task, name="task-status")
]

app_name = "todo"
