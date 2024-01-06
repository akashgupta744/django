from django.contrib import admin
from .models import *

# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic_name'] 
admin.site.register(Topic,TopicAdmin)

class WebpageAdmin(admin.ModelAdmin):
    list_display = ['topic_name', 'name', 'url', 'email']
admin.site.register(Webpage,WebpageAdmin)

class AccessAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'author']

admin.site.register(AccessRecord, AccessAdmin)