from django.urls import path
from .views import (index)

urlpatterns = [
    path("", index, name="index"),
    path("admin/", index, name="admin"),
]

app_name = "todo"