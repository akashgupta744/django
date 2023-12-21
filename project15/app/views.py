from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length


# Create your views here.
def display_dept(request):
    QLDO=Dept.objects.all()
    d={'dept':QLDO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    QLDO=Emp.objects.all().order_by('ename')
    # QLDO=Emp.objects.all().order_by('-ename')
    # QLDO=Emp.objects.all().order_by(Length('ename'))
    # QLDO=Emp.objects.all().order_by(Length('ename').desc())
    d={'emp':QLDO}
    return render(request,'display_emp.html',d)


