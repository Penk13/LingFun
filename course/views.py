from django.shortcuts import render, get_object_or_404
from .models import Course


def courses(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request, "course/courses.html", context)

def course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {
        "course": course,
    }
    return render(request, "course/course.html", context)