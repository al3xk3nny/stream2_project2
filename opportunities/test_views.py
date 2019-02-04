from django.test import TestCase
from django.contrib.auth.models import User, Group 
from .models import Post, Message
from .forms import PostForm, MessageForm

# Create your tests here.

class TestOpportunitiesViews(TestCase):
        
    
    def test_get_write_post(self):
        self.user = User.objects.create_user(username="testuser", password="pa55word")
        login = self.client.login(username="testuser", password="pa55word")
        
        page = self.client.get("/posts/add/")
        self.assertEqual(page.status_code, 200)
        
    def test_post_write_post(self):
        self.user = User.objects.create_user(username="testuser", password="pa55word")
        login = self.client.login(username="testuser", password="pa55word")
        
        page = self.client.post("/posts/add/", {"title": "testtitle", "content": "testcontent"})
        self.assertEqual(page.status_code, 302)
        post = Post.objects.latest("id")
        self.assertEqual(post.title, "testtitle")