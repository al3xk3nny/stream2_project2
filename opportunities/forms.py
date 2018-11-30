from django import forms
from .models import Post, Message

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude = ["created_date", "author", "type"]


class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        exclude = ["read", "post", "recipient", "author"]