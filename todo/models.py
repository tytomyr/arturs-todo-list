from django.db import models
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    optional_deadline = models.DateTimeField(blank=True)
    the_boolean = models.BooleanField()
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
