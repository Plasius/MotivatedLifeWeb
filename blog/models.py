from django.db import models
from django.urls import reverse
from django.utils import timezone

def find_upload(instance, filename):
    return '%s/%s' %(instance.id, filename)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 120)

    image = models.ImageField(null = True, blank = True, height_field = 'height_field', width_field = 'width_field', upload_to=find_upload)
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)

    content = models.TextField()
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    created = models.DateTimeField(auto_now = False, auto_now_add = True)
    published = models.DateField(default = timezone.now)
    draft = models.BooleanField(default = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.id})
