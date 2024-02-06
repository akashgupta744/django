from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password = None):
        if not email:
            raise ValueError('Email Required')
        nor_e = self.normalize_email(email)
        upo = self.model(email=nor_e, first_name = first_name, last_name = last_name)
        upo.set_password(password)
        upo.save()
        return upo
    
    def create_superuser(self, email, first_name, last_name, password):
        upo = self.create_user(email, first_name, last_name, password)
        upo.is_staff = True
        upo.is_superuser = True
        upo.save()
        return upo 


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name'] 

