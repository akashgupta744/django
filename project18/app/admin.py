from django.contrib import admin
from .models import*

# Register your models here.

class AdminAform(admin.ModelAdmin):
    list_display = ['username']
admin.site.register(Aform,AdminAform)


class AdminDform(admin.ModelAdmin):
    list_display = ['username', 'password', 'email_ID', 'Mobile_No', 'User_DOB']
admin.site.register(Dform, AdminDform)