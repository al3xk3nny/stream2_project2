from django.test import TestCase
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User


# Create your tests here.

class TestAccountsViews(TestCase):
    
    def test_get_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    
    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/login.html")
    
    
    def test_get_signup_page(self):
        page = self.client.get("/accounts/signup/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/signup.html")