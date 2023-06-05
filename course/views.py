from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, UserCourse, Quiz, UserQuiz
from .forms import UserQuizForm


def courses(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request, "course/courses.html", context)

def course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user = request.user
    try:
        user_course = UserCourse.objects.get(course=course, user=user)
        quizzes = Quiz.objects.filter(course=course)
    except:
        user_course = False
        quizzes = False
    
    context = {
        "course": course,
        "user_course": user_course,
        "quizzes": quizzes,
    }
    return render(request, "course/course.html", context)

@login_required
def enroll(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user = request.user
    try:
        user_course = UserCourse.objects.get(course=course, user=user)
    except:
        user_course = False

    if not user_course:
        UserCourse.objects.create(user=user, course=course)
    return redirect("course", pk=pk)

@login_required
def quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    user = request.user
    try:
        user_quiz = UserQuiz.objects.get(user=user, quiz=quiz)
    except:
        UserQuiz.objects.create(user=user, quiz=quiz)
        user_quiz = UserQuiz.objects.get(user=user, quiz=quiz)
    form = UserQuizForm(instance=user_quiz)
    if request.method == "POST":
        form = UserQuizForm(request.POST)
        if form.is_valid():
            user_quiz.answer = form.cleaned_data["answer"]
            user_quiz.is_finished = True
            user_quiz.save()
            return redirect("course", quiz.course.pk)

    context = {
        "quiz": quiz,
        "form": form,
        "user_quiz": user_quiz,
    }
    return render(request, "course/quiz.html", context)

def leaderboard(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    user_quizzes = UserQuiz.objects.all()
    context = {
        "quiz": quiz,
        "user_quizzes": user_quizzes,
    }
    return render(request, "course/leaderboard.html", context)