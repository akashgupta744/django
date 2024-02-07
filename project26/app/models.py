from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length = 100, primary_key = True)
    school_principal = models.CharField(max_length = 100)
