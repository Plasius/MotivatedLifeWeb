from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published', 'created', 'updated']
    list_filter = ['updated', 'created']
    search_fields= ['title', 'content']
    class Meta:
        model = Post

# Register your models here.
admin.site.register(Post, PostAdmin)
