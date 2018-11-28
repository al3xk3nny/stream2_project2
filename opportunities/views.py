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

def read_post(request):
    if is_in_group(request.user, "marketer"):
        to_view = "producer"
    else:
        to_view = "marketer"
    posts = Post.objects.filter(type = to_view)
    
    return render(request, "opportunities/post_list.html", {"posts": posts})


@login_required
def write_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        p = form.save(commit=False)
        p.author = request.user # Come back to this
        p.save()
        
        return redirect(read_post)
    else:
        form = PostForm()
        
        return render(request, "opportunities/post_form.html", {"form": form})