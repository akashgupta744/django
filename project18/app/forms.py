from django import forms
from app.models import *


class Aforms(forms.Form):
    username = forms.CharField(max_length=100)


class Dforms(forms.Form):
    afl = [[do.username, do.username] for do in Aform.objects.all()]
    username = forms.ChoiceField(choices = afl)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmp = forms.CharField()
    email_ID = forms.EmailField()
    Mobile_No = forms.IntegerField()
    User_DOB =  forms.DateField()
    

