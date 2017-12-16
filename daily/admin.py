from django.contrib import admin
from daily.models import QuoteProfile, Quote

class PostQuoteAdmin(admin.ModelAdmin):
    list_display= ['name']
    class Meta:
        model= Quote

class PostProfileAdmin(admin.ModelAdmin):
    list_display= ['user']
    class Meta:
        model=QuoteProfile

# Register your models here.
admin.site.register(QuoteProfile, PostProfileAdmin)
admin.site.register(Quote, PostQuoteAdmin)
