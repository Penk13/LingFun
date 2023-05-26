from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
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
    context = {
        "user": user
    }
    return render(request, "core/profile.html", context)