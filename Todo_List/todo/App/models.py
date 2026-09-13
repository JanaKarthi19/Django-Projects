from django.db import models

# Create your models here.

class User(models.Model):
    User_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=200)
    description = models.CharField(blank=True, null=True)
    Completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)