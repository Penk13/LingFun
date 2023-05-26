from django.shortcuts import render, get_object_or_404
from .models import Group, Chat


def groups(request):
    groups = Group.objects.all()
    context = {
        "groups": groups,
    }
    return render(request, "group/groups.html", context)

def group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    chats = Chat.objects.filter(group=group)
    context = {
        "group": group,
        "chats": chats,
    }
    return render(request, "group/group.html", context)