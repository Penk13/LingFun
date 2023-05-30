from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Group, Chat, UserGroup
from .forms import ChatForm


def groups(request):
    groups = Group.objects.all()
    context = {
        "groups": groups,
    }
    return render(request, "group/groups.html", context)

def group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    user = request.user
    try:
        user_group = UserGroup.objects.get(group=group, user=user)
        chats = Chat.objects.filter(group=group)
    except:
        user_group = False
        chats = False

    form = ChatForm()
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChatForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.group = group
                obj.user = user
                obj.save()
                return redirect("group", pk=pk)

    context = {
        "group": group,
        "chats": chats,
        "user_group": user_group,
        "form": form,
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