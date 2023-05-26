from django.contrib import admin
from .models import Language, Course, UserCourse, Quiz, UserQuiz

admin.site.register(Language)
admin.site.register(Course)
admin.site.register(UserCourse)
admin.site.register(Quiz)
admin.site.register(UserQuiz)
