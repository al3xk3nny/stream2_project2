from django.test import TestCase
from django.contrib.auth.models import User, Group 
from .models import Post, Message
from .forms import PostForm, MessageForm

# Create your tests here.

class TestOpportunitiesViews(TestCase):
    
    # Add Post
    
    def test_get_read_posts_page_if_producer(self):
        marketer = Group.objects.create(name="marketer")
        marketer.save()
        self.client.post("/accounts/signup/?type=marketer", {
            "username": "testuser",
            "first_name": "test",
            "last_name": "user",
            "email": "test@email.com",
            "password1": "pa55word",
            "password2": "pa55word",
            "phone_number": "+353871234567"
        })
        
        page = self.client.get("/posts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "opportunities/post_list.html")
    
    
    def test_get_read_posts_page_if_marketer(self):
        marketer = Group.objects.create(name="producer")
        marketer.save()
        self.client.post("/accounts/signup/?type=producer", {
            "username": "testuser",
            "first_name": "test",
            "last_name": "user",
            "email": "test@email.com",
            "password1": "pa55word",
            "password2": "pa55word",
            "phone_number": "+353871234567"
        })
        
        page = self.client.get("/posts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "opportunities/post_list.html")
    
    
    def test_get_my_posts_page(self):
        marketer = Group.objects.create(name="marketer")
        marketer.save()
        self.client.post("/accounts/signup/?type=marketer", {
            "username": "testuser",
            "first_name": "test",
            "last_name": "user",
            "email": "test@email.com",
            "password1": "pa55word",
            "password2": "pa55word",
            "phone_number": "+353871234567"
        })
        
        page = self.client.get("/posts/profile/posts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "opportunities/my_post_list.html")
    
    
    def test_get_my_inbox_page(self):
        marketer = Group.objects.create(name="marketer")
        marketer.save()
        self.client.post("/accounts/signup/?type=marketer", {
            "username": "testuser",
            "first_name": "test",
            "last_name": "user",
            "email": "test@email.com",
            "password1": "pa55word",
            "password2": "pa55word",
            "phone_number": "+353871234567"
        })
        
        page = self.client.get("/posts/profile/inbox/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "opportunities/inbox.html")
    
    
    
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