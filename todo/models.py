from django.db import models
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    optional_deadline = models.DateTimeField(blank=True, null=True)
    the_boolean = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")
