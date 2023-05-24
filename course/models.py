from django.db import models
from django.contrib.auth.models import User


DIFFICULTY = (
    ("BEGINNER", "Beginner"),
    ("INTERMEDIATE", "Intermediate"),
    ("ADVANCED", "Advanced"),
)


class Language(models.Model):
    name = models.CharField(max_length=255, blank=False)


class Course(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY, blank=True)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    enrolled_date = models.DateTimeField(auto_now_add=True)
