from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from .models import *
# Create your views here.



def course(request):
    if request.method =='POST':
        ci=request.POST['cid']
        cn=request.POST['cn'] 
        tn=request.POST['tn']
        co = Course.objects.get_or_create(cid=ci, cname=cn, tname=tn)[0]
        co.save()
      
    return render(request,'course.html')



def student(request):
    QLSO=Course.objects.all()
    d={'courses':QLSO}
    if request.method =='POST':
        si=request.POST['sid']
        sn=request.POST['sn'] 
        sd=request.POST['sd']
        cid=request.POST['cid']
        co = Course.objects.get(cid=cid)
        so = Student.objects.get_or_create(sid=si, sname=sn, sdob=sd, cid=co)[0]
        so.save()
    return render(request,'student.html',d)
