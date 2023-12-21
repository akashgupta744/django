from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.

def Topic_dis(request):
    QLTO=Topic.objects.all()
    d={'Topic':QLTO}
    return render(request,'Topic.html',d)

def Webpage_dis(request):
    QLWO=Webpage.objects.all()
    d={'Webpage':QLWO}
    return render(request,'Webpage.html',d)

def AccessRecord_dis(request):
    QLAO=AccessRecord.objects.all()
    d={'AccessRecord':QLAO}
    return render(request,'AccessRecord.html',d)


def insert_topic(request):
    tn=input('enter the topic name')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()

    return HttpResponse('Topic Page Update Successfully')

def insert_webpage(request):
    tn=input('enter the topic name')
    n=input('enter the name')
    u=input('enter the url')
    e=input('enter the email')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()

    return HttpResponse(' WEBPage Update Successfully')


def insert_access(request):
    pk=int(input('enter Pk Value of webpages'))
    d=input('enter date')
    a=input('enter the author')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    NAO.save()

    return HttpResponse('accesspage Update Successfully')

def update_webpage(request):
    Webpage.objects.filter(name='rajan').update(email='ra123@gmail.com')
    Webpage.objects.filter(name='ranjan').update(email='ra123@gmail.com',name='ranjan')
    Webpage.objects.filter(name='ranjan').update(topic_name='hockey')

    UWO=Topic.objects.get_or_create(topic_name='hockey')[0]
    UWO.save()

    Webpage.objects.update_or_create(name='rohit', defaults={'topic_name':UWO})    

    # Webpage.objects.update_or_create(name__startswith='r', defaults={'topic_name':UWO})
    UWOB=Topic.objects.get_or_create(topic_name='basketball')[0]
    UWOB.save()
    Webpage.objects.update_or_create(name='akku', defaults={'topic_name':UWOB, 'url':'http://messi.in'})    
    
    QLUWO=Webpage.objects.all()
    d={'Webpage':QLUWO}
    return render(request,'Webpage.html',d)