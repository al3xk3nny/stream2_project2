from django.urls import path

from opportunities.views import read_post, write_post

urlpatterns = [
    path("add/", write_post, name="write_post"),
    path("", read_post, name="read_post"),  
]