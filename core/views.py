from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from course.models import Course, UserCourse, Quiz, UserQuiz
from group.models import Group, Chat, UserGroup


def home(request):
    return render(request, "core/home.html")

def about_us(request):
    return render(request, "core/about_us.html")

def services(request):
    return render(request, "core/services.html")

def terms_of_service(request):
    return render(request, "core/terms_of_service.html")

def privacy_policy(request):
    return render(request, "core/privacy_policy.html")

@login_required
def profile(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user=user)
    user_groups = UserGroup.objects.filter(user=user)
    context = {
        "user": user,
        "user_courses": user_courses,
        "user_groups": user_groups,
    }
    return render(request, "core/profile.html", context)