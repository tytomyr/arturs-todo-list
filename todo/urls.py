from django.urls import path
from .views import (TagListView,
                    TaskListView,
                    TagCreateView,
                    TagDeleteView,)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("admin/", TaskListView.as_view(), name="admin"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete")
]

app_name = "todo"
