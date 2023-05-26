from django.contrib import admin
from .models import Group, UserGroup, Chat

admin.site.register(Group)
admin.site.register(UserGroup)
admin.site.register(Chat)
