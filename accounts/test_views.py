from django.test import TestCase
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User, Group 


# Create your tests here.

class TestAccountsViews(TestCase):
    
    # Index
    
    def test_get_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    
    # Log in
    
    def test_get_log_in_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/login.html")
    
    
    def test_user_can_log_in(self):
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
        
        response = self.client.post("/", {
            "username": "testuser",
            "password": "pa55word"
        })
        
        self.assertRedirects(response, "/posts/", status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
    
    
    def test_user_can_log_out(self):
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
        
        response = self.client.get("/accounts/logout/")
        
        self.assertRedirects(response, "/", status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
    
    
    def test_error_on_log_in(self):
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
        
        response = self.client.post("/accounts/login/", {
            "username": "test",
            "password": "pa55word"
        })
        
        self.assertFormError(response, "form", None, "Please enter a correct username and password. Note that both fields may be case-sensitive.")
    
    
    # Sign up
    
    def test_get_signup_page(self):
        page = self.client.get("/accounts/signup/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/signup.html")
    
    
    def test_user_can_sign_up(self):
        marketer = Group.objects.create(name="marketer")
        marketer.save()
        response = self.client.post("/accounts/signup/?type=marketer", {
            "username": "testuser",
            "first_name": "test",
            "last_name": "user",
            "email": "test@email.com",
            "password1": "pa55word",
            "password2": "pa55word",
            "phone_number": "+353871234567"
        })
        self.assertRedirects(response, '/posts/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
    
    
    # Profile
    
    def test_get_profile_page(self):
        marketer = Group.objects.create(name="marketer")
        marketer.save()
        response = self.client.post("/accounts/signup/?type=marketer", {
            "username": "testuser",
            "first_name": "test",
            "last_name": "user",
            "email": "test@email.com",
            "password1": "pa55word",
            "password2": "pa55word",
            "image": "avatars/anonymous.png",
            "phone_number": "+353871234567"
        })
        
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")