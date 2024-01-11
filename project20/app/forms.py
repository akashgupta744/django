from django import forms
from .models import *

class Schoolform(forms.Form):
    scode = forms.IntegerField(label = 'school code', widget=forms.NumberInput(attrs={'placeholder':'Enter school code'}))
    sname = forms.CharField(max_length=100, label = 'school name', widget=forms.TextInput(attrs={'placeholder':'Enter school name'}))
    sprinc = forms.CharField(max_length = 100, label = 'principal name', widget=forms.TextInput(attrs={'placeholder':'Enter principal name'}))
    sloc = forms.CharField(max_length = 100, label = 'school location', widget=forms.TextInput(attrs={'placeholder':'Enter school location'}))
    semail = forms.EmailField(label = 'email id', widget=forms.EmailInput(attrs={'placeholder':'Enter email'}))
    cemail = forms.EmailField(label = 'confirm email id', widget=forms.EmailInput(attrs={'placeholder':'Enter confirm email'}))
    passw = forms.CharField(max_length = 100, label = 'password', widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    cpassw = forms.CharField(max_length = 100, label = ' confirm password', widget=forms.PasswordInput(attrs={'placeholder':'Enter confirm password'}))
    botcatcher = forms.CharField(required=False, widget = forms.HiddenInput)

    def clean(self):
        print(self.cleaned_data)
        se = self.cleaned_data['semail']
        ce = self.cleaned_data['cemail']
        pa = self.cleaned_data['passw']
        cp = self. cleaned_data['cpassw']


        if se != ce or pa != cp:
            raise forms.ValidationError('invalid data')

    def clean_botcatcher(self):
        b = self.cleaned_data['botcatcher']
        if len(b) > 0:
            raise forms.ValidationError('invalid data')
        
        
        