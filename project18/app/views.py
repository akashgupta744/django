from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def aform(request):
    aobj = Aforms()

    if request.method == 'POST':
       
        afdo = Aforms(request.POST) 
       
        if afdo.is_valid():
            un = afdo.cleaned_data['username']
            
            afo = Aform.objects.get_or_create(username=un)[0]
            afo.save()
    return render(request,'aform.html', {'aobj':aobj})



def dform(request):
    dobj = Dforms()

    if request.method == 'POST':
        dfdo = Dforms(request.POST)
        if dfdo.is_valid():
            un = dfdo.cleaned_data['username']
            uno = Aform.objects.get(username= un)
            pw = dfdo.cleaned_data['password']
            cpw = dfdo.cleaned_data['confirmp']
            eid = dfdo.cleaned_data['email_ID']
            mob = dfdo.cleaned_data['Mobile_No']
            dob = dfdo.cleaned_data['User_DOB']
            afo = Dform.objects.get_or_create(username=uno, password=pw, confirmp=cpw, email_ID=eid, Mobile_No=mob, User_DOB=dob)[0]
            afo.save() 
    return render(request,'djform.html', {'dobj':dobj})

