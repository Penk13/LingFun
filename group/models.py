from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


class UserGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
