from django.db import models

# Create your models here.

class Country(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)
    ccode=models.IntegerField()
    cpopulation=models.IntegerField()

    def __str__(self):
        return self.cname
    
class Capital(models.Model):
    caname=models.CharField(max_length=100, primary_key=True)
    cacode=models.IntegerField()
    cname=models.OneToOneField(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.caname
