from django.test import TestCase
from .forms import CreditCardForm

# Create your tests here.

class TestBillingForms(TestCase):
    
    # Add Credit Card Form
    
    def test_credit_card_form(self):
        
        form=CreditCardForm({
            "credit_card_number": "4242424242424242",
            "cvv": "100",
            "expiry_month": 10,
            "expiry_year": 2019,
            "stripe_id": "something"
        })
        self.assertTrue(form.is_valid())