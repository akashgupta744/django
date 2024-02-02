from django.shortcuts import render
from .models import *
from django.db.models import Q
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


def self_joins(request):
    SJQLO = Emp.objects.select_related('mgr').all()
    SJQLO = Emp.objects.select_related('mgr').filter(hiredate='2024-01-10')
    SJQLO = Emp.objects.select_related('mgr').filter(hiredate__in=('2024-01-10','2024-01-11','2024-01-12'))
    SJQLO = Emp.objects.select_related('mgr').filter(sal__gt=2500)
    SJQLO = Emp.objects.select_related('mgr').filter(sal__gte=2500)
    SJQLO = Emp.objects.select_related('mgr').filter(sal__lt=2500)
    SJQLO = Emp.objects.select_related('mgr').filter(sal__lte=2500)
    SJQLO = Emp.objects.select_related('mgr').filter(hiredate__month='01')
    SJQLO = Emp.objects.select_related('mgr').filter(mgr__empno = 7698)
    SJQLO = Emp.objects.select_related('mgr').filter(mgr = 7698)
    SJQLO = Emp.objects.select_related('mgr').filter(mgr__empno = 7698, comm__isnull = True)
    SJQLO = Emp.objects.select_related('mgr').filter(mgr__empno = 7698, comm__isnull = False)
    SJQLO = Emp.objects.select_related('mgr').filter(ename__startswith = 'A')
    SJQLO = Emp.objects.select_related('mgr').filter(ename__endswith = 'G')
    SJQLO = Emp.objects.select_related('mgr').filter(ename__contains = 'A')
    SJQLO = Emp.objects.select_related('mgr').filter(Q(comm__isnull = True) | Q(ename__startswith = 'A'))
    SJQLO = Emp.objects.select_related('mgr').filter(Q(ename__startswith = 'S') | Q(comm__isnull = True) )
    
    d={'SJQLO':SJQLO}
    return render(request, 'self_joins.html',d)

def multiple_joins(request):
    EMD = Emp.objects.select_related('deptno', 'mgr').all()
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(hiredate__in=('2024-01-10','2024-01-11','2024-01-12'))
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(sal__gt=2500)
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(sal__gte=2500)
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(sal__lt=2500)
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(sal__lte=2500)
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(deptno=10, comm = None, ename = 'CLARK')
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(deptno__dname='ACCOUNTING', ename = 'CLARK')
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(deptno__dname='ACCOUNTING', ename = 'CLARK', deptno__loc = 'NEW YORK')
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(deptno__dname='ACCOUNTING', comm__isnull = True)
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(comm__isnull = True)
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(comm__isnull = False)
    EMD = Emp.objects.prefetch_related('deptno', 'mgr').all()
    EMD = Emp.objects.prefetch_related('deptno', 'mgr').filter(deptno=10)
    EMD = Emp.objects.prefetch_related('deptno', 'mgr').filter(deptno__dname='ACCOUNTING', ename = 'CLARK', deptno__loc = 'NEW YORK')
    EMD = Emp.objects.prefetch_related('deptno', 'mgr').filter(deptno__dname='ACCOUNTING', comm__isnull = True)
    EMD = Emp.objects.prefetch_related('deptno', 'mgr').filter(comm__isnull = True)
    EMD = Emp.objects.prefetch_related('deptno', 'mgr').filter(comm__isnull = False)
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(hiredate__month='01')
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(mgr__empno = 7698) 
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(mgr = 7698)
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(mgr__empno = 7698, comm__isnull = True)
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(mgr__empno = 7698, comm__isnull = False)
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(ename__startswith = 'A')
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(ename__endswith = 'G')
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(ename__contains = 'A')
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(Q(comm__isnull = True) | Q(ename__startswith = 'A'))
    EMD = Emp.objects.select_related('deptno', 'mgr').filter(Q(ename__startswith = 'S') | Q(comm__isnull = True) )
    

    d = {'EMD':EMD}
    return render(request, 'multiple_joins.html',d)
