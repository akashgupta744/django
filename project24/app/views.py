from django.shortcuts import render
from .models import *
# Create your views here.

def equi_joins(request):
    QLTO = Emp.objects.select_related('deptno').all()
    QLTO = Emp.objects.select_related('deptno').filter(deptno=10)
    QLTO = Emp.objects.select_related('deptno').filter(deptno=10, ename = 'KING')
    QLTO = Emp.objects.select_related('deptno').filter(deptno=10, comm = None, ename = 'CLARK')
    QLTO = Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING', ename = 'CLARK')
    QLTO = Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING', ename = 'CLARK', deptno__loc = 'NEW YORK')
    QLTO = Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING', comm__isnull = True)
    QLTO = Emp.objects.select_related('deptno').filter(comm__isnull = True)
    QLTO = Emp.objects.select_related('deptno').filter(comm__isnull = False)

    QLTO = Emp.objects.prefetch_related('deptno').all()
    QLTO = Emp.objects.prefetch_related('deptno').filter(deptno=10)
    QLTO = Emp.objects.prefetch_related('deptno').filter(deptno__dname='ACCOUNTING', ename = 'CLARK', deptno__loc = 'NEW YORK')
    QLTO = Emp.objects.prefetch_related('deptno').filter(deptno__dname='ACCOUNTING', comm__isnull = True)
    QLTO = Emp.objects.prefetch_related('deptno').filter(comm__isnull = True)
    QLTO = Emp.objects.prefetch_related('deptno').filter(comm__isnull = False)
    d = {'QLTO':QLTO}
    return render(request, 'equi_joins.html', d)