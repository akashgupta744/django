from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(default = 'john doe (default)', max_length=200, null=True)

    title = models.CharField(default = 'This is the default, title change it in profile', max_length=200, null=True)

    desc_text = 'Hey, there this is a default text description about you that you can change on after clicking on "Edit"'

    desc = models.CharField(default = desc_text, max_length=200, null= True)

    profile_img = models.ImageField(default= 'media/default.jpg',upload_to='media', null = True, blank =True)

    def __str__(self):
        return self.name