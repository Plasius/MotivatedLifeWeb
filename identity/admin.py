from django.contrib import admin
from identity.models import IdentityProfile

class PostIdentityProfileAdmin(admin.ModelAdmin):
    list_display= ['user']
    search_fields= ['user']
    class Meta:
        model= IdentityProfile

# Register your models here.
admin.site.register(IdentityProfile, PostIdentityProfileAdmin)
