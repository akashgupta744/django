from django.shortcuts import render

# Create your views here.
def ifcondition(request):
    return render(request,'index.html',{'a':5,'b':10,'c':15,'d':20})
