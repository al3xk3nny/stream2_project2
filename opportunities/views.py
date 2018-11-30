from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Message
from .forms import PostForm, MessageForm
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
    messages = Message.objects.filter(recipient=request.user)
    
    return render(request, "opportunities/inbox.html", {"messages": messages})


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
        
        return redirect(read_posts)
    else:
        form = PostForm()
        
        return render(request, "opportunities/post_form.html", {"form": form})


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        form.save()
        
        return redirect(your_posts)
    else:
        form = PostForm(instance=post)
        
        return render(request, "opportunities/post_edit_form.html", {"form": form})


@login_required
def write_message(request, id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=id)
        form = MessageForm(request.POST, request.FILES)
        m = form.save(commit=False)
        m.author = request.user
        m.recipient = post.author
        m.save()
        
        return redirect(read_posts)
    else:
        form = MessageForm()
        
        return render(request, "opportunities/message_form.html", {"form": form})