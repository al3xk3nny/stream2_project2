from django.urls import path

from opportunities.views import read_posts, your_posts, show_inbox, write_post, edit_post, write_message

urlpatterns = [
    path("", read_posts, name="read_posts"),
    
    path("profile/posts/", your_posts, name="your_posts"),
    
    path("profile/inbox/", show_inbox, name="show_inbox"),
    
    path("add/", write_post, name="write_post"),
    
    path("<int:id>/edit", edit_post, name="edit_post"),
    
    path("send/<int:id>", write_message, name="write_message"),
]