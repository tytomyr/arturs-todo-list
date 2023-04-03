from django.urls import path
from .views import (TagListView,
                    TaskListView)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("admin/", TaskListView.as_view(), name="admin"),
    path("tags/", TagListView.as_view(), name="tags"),
]

app_name = "todo"
