from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def read_post(request):
    posts = Post.objects.filter(created_date__lte = timezone.now())
    
    return render(request, "opportunities/post_list.html", {"posts": posts})


@login_required
def write_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        p = form.save(commit=False)
        p.author = request.user
        p.save()
        
        return redirect(read_post)
    else:
        form = PostForm()
        
        return render(request, "opportunities/post_form.html", {"form": form})