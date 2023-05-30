from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Group, Chat, UserGroup


def groups(request):
    groups = Group.objects.all()
    context = {
        "groups": groups,
    }
    return render(request, "group/groups.html", context)

def group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    chats = Chat.objects.filter(group=group)
    user = request.user
    try:
        user_group = UserGroup.objects.get(group=group, user=user)
    except:
        user_group = False

    context = {
        "group": group,
        "chats": chats,
        "user_group": user_group,
    }
    return render(request, "group/group.html", context)

@login_required
def join_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    user = request.user
    try:
        user_group = UserGroup.objects.get(group=group, user=user)
    except:
        user_group = False

    if not user_group:
        UserGroup.objects.create(user=user, group=group)
    return redirect("group", pk=pk)
