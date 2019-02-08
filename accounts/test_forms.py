from django.test import TestCase
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User

# Create your tests here.

class TestAccountsSignUpForm(TestCase):
    
    # Sign Up Form
    
    def test_signup_form(self):
        
        form=SignUpForm({
            "username": "testuser",
            "first_name": "test",
            "last_name": "user",
            "email": "testuser@example.com",
            "password1": "PasswordForTest",
            "password2": "PasswordForTest"
        })
        self.assertTrue(form.is_valid())
    
    
    def test_can_not_create_a_user_with_just_username_and_password(self):
        
        form=SignUpForm({
            "username": "testuser",
            "password1": "PasswordForTest",
            "password2": "PasswordForTest"
        })
        self.assertFalse(form.is_valid())
    
    
    def test_correct_message_for_missing_username(self):
        
        form=SignUpForm({
            "username": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"], [u"This field is required."])
    
    
    def test_correct_message_for_missing_first_name(self):
        
        form=SignUpForm({
            "first_name": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["first_name"], [u"This field is required."])
    
    
    def test_correct_message_for_missing_last_name(self):
        
        form=SignUpForm({
            "last_name": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["last_name"], [u"This field is required."])
    
    
    def test_correct_message_for_missing_email(self):
        
        form=SignUpForm({
            "email": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["email"], [u"This field is required."])
    
    
    def test_correct_message_for_missing_password1(self):
        
        form=SignUpForm({
            "password1": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["password1"], [u"This field is required."])
    
    
    def test_correct_message_for_missing_password2(self):
        
        form=SignUpForm({
            "password2": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["password2"], [u"This field is required."])
    
    
    def test_correct_message_for_unmatched_passwords(self):
        
        form=SignUpForm({
            "password1": "pa55word1",
            "password2": "pa55word2"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["password2"], [u"The two password fields didn't match."])
    
    
    # Profile form
    
    def test_profile_form(self):
        
        form=ProfileForm({
            "phone_number": "+353851234567"
        })
        self.assertTrue(form.is_valid())
    
    
    def test_correct_message_for_missing_phone_number(self):
        
        form=ProfileForm({
            "phone_number": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["phone_number"], [u"This field is required."])
    
    
    def test_correct_message_for_phone_number_Wrong_format(self):
        
        form=ProfileForm({
            "phone_number": "00353 85 1234567"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["phone_number"], [u"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."])
