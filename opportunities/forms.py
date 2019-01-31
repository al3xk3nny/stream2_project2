from django import forms
from .models import Post, Message

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude = ["created_date", "author", "type"]
        widgets = {
                    "title": forms.TextInput(attrs={"placeholder": "Brand A"}),
                    "content": forms.Textarea(attrs={"placeholder": "I'm looking for..."}),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        exclude = ["read", "post", "recipient", "author"]
        widgets = {
                    "title": forms.TextInput(attrs={"placeholder": "Brand B"}),
                    "content": forms.Textarea(attrs={"placeholder": "I'm interested in your opportunity..."}),
        }