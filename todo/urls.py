from django.urls import path
from .views import (index,
                    TagListView,
                    TaskListView)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("admin/", index, name="admin"),
    path("tags/", TagListView.as_view(), name="tags"),
]

app_name = "todo"
