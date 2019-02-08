from django.test import TestCase
from django.contrib.auth.models import User, Group 

# Create your tests here.

class TestBillingViews(TestCase):
    
    # Add Credit Card
    
    def test_get_add_credit_card_page(self):
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
        
        page = self.client.get("/billing/add_credit_card/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "billing/add_credit_card.html")
    
    
   # Subscribe
    
    def test_get_subscribe_page(self):
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
        
        page = self.client.get("/billing/subscribe/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "billing/subscribe.html")