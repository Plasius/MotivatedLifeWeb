from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

	

# Create your models here.
class IdentityProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.DO_NOTHING)
    age= models.IntegerField(default=0)