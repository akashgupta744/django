from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.dname
    
    
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    mgr=models.IntegerField()
    sal=models.IntegerField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
    