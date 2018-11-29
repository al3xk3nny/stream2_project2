from django.urls import path

from opportunities.views import read_posts, your_posts, write_post

urlpatterns = [
    path("", read_posts, name="read_posts"),
    
    path("profile/posts/", your_posts, name="your_posts"),
    
    path("add/", write_post, name="write_post"),
]