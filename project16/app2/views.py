from django.shortcuts import render
from app2.models import *
from django.db.models.functions import Length
from django.db.models import Q


# Create your views here.
def display_dept(request):
    QLDO=Dept.objects.all()
    d={'dept':QLDO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    QLDO=Emp.objects.all()
    d={'emp':QLDO}
    return render(request,'display_emp.html',d)


