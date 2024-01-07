from django.db import models

# Create your models here.

class Aform(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.username
    

class Dform(models.Model):
    username = models.ForeignKey(Aform, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    confirmp = models.CharField(max_length=100)
    email_ID = models.EmailField(max_length=100)
    Mobile_No = models.IntegerField()
    User_DOB =  models.DateField()


