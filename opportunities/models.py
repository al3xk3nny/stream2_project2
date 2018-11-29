from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    type = models.CharField(max_length=10, default="marketer", null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='posts', null=False, default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    
    def __str__(self):
        return self.title


class Message(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    read = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='messages', null=False, default=1, on_delete=models.SET_DEFAULT)
    recipient = models.ForeignKey(User, related_name='messages_received', null=False, default=1, on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(User, related_name='messages_sent', null=False, default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    
    def __str__(self):
        return self.title