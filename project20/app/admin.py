from django.contrib import admin
from .models import *

# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['scode', 'sname', 'sprinc', 'sloc', 'cemail', 'cpassw']


admin.site.register(School, SchoolAdmin)
