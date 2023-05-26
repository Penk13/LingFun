from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


DIFFICULTY = (
    ("BEGINNER", "Beginner"),
    ("INTERMEDIATE", "Intermediate"),
    ("ADVANCED", "Advanced"),
)


class Language(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Course(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='course_img/', default='course_img/default_course_img.png')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY, blank=True)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    content = models.TextField(blank=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.title + " - " + self.user.username


class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    question = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer = models.TextField(blank=True)
    is_finished = models.BooleanField(default=False)
    score = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(0, message='Score cannot be less than 0.'),
        MaxValueValidator(100, message='Score cannot be greater than 100.')
    ])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quiz.name + " - " + self.user.username
