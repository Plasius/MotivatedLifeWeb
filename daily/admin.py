from django.contrib import admin
from daily.models import QuoteProfile, Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display= ['day','name']
    search_fields= ['day', 'name']
    class Meta:
        model= Quote

class ProfileAdmin(admin.ModelAdmin):
    list_display= ['user']
    search_fields= ['user']
    class Meta:
        model = QuoteProfile

# Register your models here.
admin.site.register(QuoteProfile, ProfileAdmin)
admin.site.register(Quote, QuoteAdmin)
