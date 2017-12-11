from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserQuoteProfile(models.Model):
    user= models.OneToOneField(User)
    progress= models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    if(kwargs['created']):
        user_profile= UserQuoteProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
