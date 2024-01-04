from django.db import models

# Create your models here.

class Course(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)
    tname=models.CharField(max_length=100)
    
    def __str__(self):
        return self.cname

class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    sdob=models.DateField()
    cid=models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.sname


class Login(models.Model):
    user_name=models.CharField(max_length = 150, primary_key=True)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user_name




















































































































































