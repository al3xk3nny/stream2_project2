from django.test import TestCase
from .forms import PostForm, MessageForm

# Create your tests here.

class TestOpportunitiesForms(TestCase):
    
    def test_post_form(self):
        
        form=PostForm({
            "title": "testtitle",
            "content": "testcontent",
            "type": "testtype"
        })
        self.assertTrue(form.is_valid())
    
        
    def test_message_form(self):
        
        form=MessageForm({
            "title": "testtitle",
            "content": "testcontent",
            "type": "testtype"
        })
        self.assertTrue(form.is_valid())