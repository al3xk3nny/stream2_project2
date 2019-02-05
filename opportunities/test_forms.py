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
    
    
    def test_post_form_correct_message_for_missing_title(self):
        
        form=PostForm({
            "title": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"], [u"This field is required."])
    
    
    def test_post_form_correct_message_for_missing_content(self):
        
        form=PostForm({
            "content": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["content"], [u"This field is required."])
    
    
    def test_message_form(self):
        
        form=MessageForm({
            "title": "testtitle",
            "content": "testcontent",
            "type": "testtype"
        })
        self.assertTrue(form.is_valid())
    
    
    def test_message_form_correct_message_for_missing_title(self):
        
        form=MessageForm({
            "title": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"], [u"This field is required."])
    
    
    def test_message_form_correct_message_for_missing_content(self):
        
        form=MessageForm({
            "content": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["content"], [u"This field is required."])