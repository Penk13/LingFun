from django.contrib import admin
from .models import Language, Course, UserCourse

admin.site.register(Language)
admin.site.register(Course)
admin.site.register(UserCourse)
