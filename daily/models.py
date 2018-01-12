from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import random

# Create your models here.
class QuoteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    progress = models.IntegerField(default = 0)
    currentDay = models.IntegerField(default = 1)

    updated = models.DateField(blank = True, null= True)
    
    favoritesCount = models.IntegerField(default = 0)
    seenCount = models.IntegerField(default = 0)

    seen = models.TextField(default = '', blank = True)
    favorites = models.TextField(default = '', blank = True)


def create_profile(sender, **kwargs):
    if(kwargs['created']):
        user_profile= QuoteProfile.objects.create(user=kwargs['instance'])

# when a new user is registered creates a profile for it
post_save.connect(create_profile, sender=User)


class Quote(models.Model):
    name = models.CharField(max_length=300, default='', unique=True)
    day = models.IntegerField(default = 0, unique=True)
