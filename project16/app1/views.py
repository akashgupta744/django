from django.shortcuts import render
from app1.models import*

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
