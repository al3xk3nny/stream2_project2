from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY




# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to="avatars", default="avatars/anonymous.png", null=False, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False) # validators should be a list
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    stripe_id = models.CharField(max_length=80, blank=True, null=True)
    card_ending = models.CharField(max_length=4, blank=True, null=True)
    subscription_id = models.CharField(max_length=80, blank=True, null=True)
    
    @property
    def active_subscription(self):
        if self.subscription_id:
            subscription = stripe.Subscription.retrieve(self.subscription_id)
            return subscription.plan.active
        else:
            return False
    
    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)