from django import forms
from .models import *

class Topicform(forms.ModelForm):
    class Meta():
        model = Topic
        fields = '__all__'


class Webpageform(forms.ModelForm):
    class Meta():
        model = Webpage
        fields = '__all__'

class AccessRecordform(forms.ModelForm):
    class Meta():
        model = AccessRecord
        fields = '__all__'