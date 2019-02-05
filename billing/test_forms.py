from django.test import TestCase
from .forms import CreditCardForm

# Create your tests here.

class TestBillingForms(TestCase):
    
    def test_credit_card_form(self):
        
        form=CreditCardForm({
            "credit_card_number": "4242424242424242",
            "cvv": "100",
            "stripe_id": "123456789"
        })
        self.assertTrue(form.is_valid())