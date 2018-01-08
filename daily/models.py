from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class QuoteProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.DO_NOTHING)
    progress= models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    if(kwargs['created']):
        user_profile= QuoteProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Quote(models.Model):
    name = models.CharField(max_length=300, default='', unique=True)
