from django.test import TestCase
from django.contrib.auth.models import User, Group 
from .models import Post, Message
from .forms import PostForm, MessageForm

# Create your tests here.

class TestOpportunitiesViews(TestCase):
    
    
    
    def test_user_can_register(self):
        marketer = Group.objects.create(name='marketer')
        marketer.save()
        response = self.client.post("/accounts/signup/?type=marketer", {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test@email.com',
            'password1': 'Pa55word',
            'password2': 'Pa55word',
            'phone_number': '+353871234567'
        })
        self.assertRedirects(response, '/posts/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)    
    
    # Add Post
    
    def test_get_write_post(self):
        test_user = User.objects.create_user(username="testuser", email="test@example.com", password="pa55word")
        self.client.login(username="testuser", password="pa55word")
        
        page = self.client.get("/posts/add/")
        self.assertEqual(page.status_code, 200)
    
    
    def test_post_write_post(self):
        test_user = User.objects.create_user(username="testuser", email="test@example.com", password="pa55word")
        self.client.login(username="testuser", password="pa55word")
        
        page = self.client.post("/posts/add/", {"title": "testtitle", "content": "testcontent"})
        self.assertEqual(page.status_code, 302)
        post = Post.objects.latest("id")
        self.assertEqual(post.title, "testtitle")
    
    # Edit Post
    
    def test_get_edit_post_does_not_exist(self):
        test_user = User.objects.create_user(username="testuser", email="test@example.com", password="pa55word")
        self.client.login(username="testuser", password="pa55word")
        
        page = self.client.get("/posts/99/edit", {"title": "testtitle", "content": "testcontent"})
        self.assertEqual(page.status_code, 404)
    
    
    def test_post_edit_post_does_not_exist(self):
        test_user = User.objects.create_user(username="testuser", email="test@example.com", password="pa55word")
        self.client.login(username="testuser", password="pa55word")
        
        page = self.client.post("/posts/99/edit", {"title": "testtitle", "content": "testcontent"})
        self.assertEqual(page.status_code, 404)
    
    
    def test_get_edit_post_that_exists(self):
        test_user = User.objects.create_user(username="testuser", email="test@example.com", password="pa55word")
        self.client.login(username="testuser", password="pa55word")
        
        post=Post(title = "testtitle", content = "testcontent", author=test_user)
        post.save()
        
        page = self.client.get("/posts/{0}/edit".format(post.id), {"title": "testtitle", "content": "testcontent"})
        self.assertEqual(page.status_code, 200)
    
    
    def test_post_edit_post_that_exists(self):
        test_user = User.objects.create_user(username="testuser", email="test@example.com", password="pa55word")
        self.client.login(username="testuser", password="pa55word")
        
        post=Post(title = "testtitle", content = "testcontent", author=test_user)
        post.save()
        
        page = self.client.post("/posts/{0}/edit".format(post.id), {"title": "testtitle", "content": "testcontent"})
        self.assertEqual(page.status_code, 302)