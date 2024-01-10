from django.shortcuts import render,HttpResponse
from .forms import *
from .models import *
# Create your views here.

def school(request):
    sobj = Schoolform()
    d= {'sobj' : sobj}
    if request.method == 'POST':
        sfdo = Schoolform(request.POST)
        if sfdo.is_valid():
            sc = sfdo.cleaned_data['scode']
            sn = sfdo.cleaned_data['sname']
            sp = sfdo.cleaned_data['sprinc']
            sl = sfdo.cleaned_data['sloc']
            se = sfdo.cleaned_data['semail']
            ce = sfdo.cleaned_data['cemail']
            pa = sfdo.cleaned_data['passw']
            cp = sfdo.cleaned_data['cpassw']

            sfo = School.objects.get_or_create(scode = sc, sname = sn, sprinc = sp, sloc= sl, semail = se, cemail = ce, passw = pa, cpassw = cp)[0]
            sfo.save()
            return HttpResponse('school details submited')
        else:
            return HttpResponse('invalid data')
        
    return render(request, 'school.html', d)