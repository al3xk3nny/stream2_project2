from django.urls import path

from opportunities.views import read_posts, my_posts, my_inbox, write_post, edit_post, delete_post, write_message, delete_message

urlpatterns = [
    path("", read_posts, name="read_posts"),
    
    path("profile/posts/", my_posts, name="my_posts"),
    
    path("profile/inbox/", my_inbox, name="my_inbox"),
    
    path("add/", write_post, name="write_post"),
    
    path("<int:id>/edit", edit_post, name="edit_post"),
    
    path("delete/", delete_post, name="delete_post"),
    
    path("send/<int:id>", write_message, name="write_message"),
    
    path("profile/inbox/delete/", delete_message, name="delete_message"),
]