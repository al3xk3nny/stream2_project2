from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User


# Helper for checking group type.

def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


# Create your views here.

def read_posts(request):
    if is_in_group(request.user, "marketer"):
        to_view = "producer"
    else:
        to_view = "marketer"
    posts = Post.objects.filter(type = to_view)
    
    return render(request, "opportunities/post_list.html", {"posts": posts})


def your_posts(request):
    posts = Post.objects.filter(author=request.user)
    
    return render(request, "opportunities/your_post_list.html", {"posts": posts})


def show_inbox(request):
    
    return render(request, "opportunities/inbox.html")


@login_required
def write_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        p = form.save(commit=False)
        if is_in_group(request.user, "marketer"):
            p.type = "marketer"
        else:
            p.type = "producer"
        p.author = request.user
        p.save()
        
        return redirect(read_post)
    else:
        form = PostForm()
        
        return render(request, "opportunities/post_form.html", {"form": form})