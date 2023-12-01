from django.shortcuts import render

# Create your views here.

def bootstrap(request):
    return render(request,'bootstrap.html')

def bootstrap_dwnld(request):
    return render(request,'bootstrap_dwnld.html')

def bootstrap_module(request):
    return render(request,'bootstrap_module.html')

def bootstrap_mdb(request):
    return render(request,'bootstrap_mdb.html')

