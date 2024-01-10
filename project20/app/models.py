from django.db import models

# Create your models here.


class School(models.Model):
    scode = models.IntegerField(primary_key = True)
    sname = models.CharField(max_length=100)
    sprinc = models.CharField(max_length = 100)
    sloc = models.CharField(max_length = 100)
    semail = models.EmailField(null= True)
    cemail = models.EmailField(null= True)
    passw = models.CharField(max_length = 100, null= True)
    cpassw = models.CharField(max_length = 100, null= True)

    def __str__(self):
        return self.sname

    
