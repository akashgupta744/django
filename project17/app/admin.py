from django.contrib import admin
from app.models import*
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=['cid','cname','tname']
    
admin.site.register(Course,CourseAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['sid','sname','sdob','cid']

admin.site.register(Student,StudentAdmin)

class loginAdmin(admin.ModelAdmin):
    list_display=['user_name','password']

admin.site.register(Login,loginAdmin)